from __future__ import print_function

import sys

if sys.version >= '3':
    long = int

from pyspark.sql import SparkSession

# $example on$
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.sql import Row
from pyspark.sql.types import DoubleType

# $example off$

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("ALSExample") \
        .getOrCreate()

    rank = 10
    numIterations = 10
    regParam = 0.11

    # $example on$
    lines = spark.read.text("sample_movielens_ratings.txt").rdd
    parts = lines.map(lambda row: row.value.split("::"))
    ratingsRDD = parts.map(lambda p: Row(user=int(p[0]), item=int(p[1]),
                                         rating=float(p[2])))
    ratings = spark.createDataFrame(ratingsRDD)
    ratings.rating = ratings.rating.cast(DoubleType())
    (training, test) = ratings.randomSplit([0.8, 0.2])

    alsExplicit = ALS()
    defaultModel = alsExplicit.fit(training)

    paramMapExplicit = ParamGridBuilder() \
        .addGrid(alsExplicit.rank, [8, 12]) \
        .addGrid(alsExplicit.maxIter, [10, 15]) \
        .addGrid(alsExplicit.regParam, [1.0, 10.0]) \
        .build()

    evaluatorR = RegressionEvaluator(metricName="rmse", labelCol="rating")

    cvExplicit = CrossValidator(estimator=alsExplicit, estimatorParamMaps=paramMapExplicit, evaluator=evaluatorR)
    cvModelExplicit = cvExplicit.fit(training)

    predsExplicit = cvModelExplicit.bestModel.transform(test)
    predsExplicit.show()

    spark.stop()
