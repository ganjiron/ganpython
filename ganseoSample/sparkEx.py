from __future__ import print_function

import sys

if sys.version >= '3':
    long = int

from pyspark.sql import SparkSession

# $example on$
from pyspark.sql import Row
from pyspark.sql.types import DoubleType


# $example off$
def recommendation(train):
    from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
    from pyspark.ml.evaluation import BinaryClassificationEvaluator

    from pyspark.ml.recommendation import ALS

    alsImplicit = ALS(implicitPrefs=True)

    # model=als.fit(train)

    paramMapImplicit = ParamGridBuilder() \
        .addGrid(alsImplicit.rank, [20, 120]) \
        .addGrid(alsImplicit.maxIter, [10, 15]) \
        .addGrid(alsImplicit.regParam, [0.01, 1.0]) \
        .addGrid(alsImplicit.alpha, [10.0, 40.0]) \
        .build()

    evaluator = BinaryClassificationEvaluator(rawPredictionCol="prediction", labelCol="rating",
                                              metricName="areaUnderROC")

    # Build the recommendation model using ALS on the training data

    # als = ALS(rank=120, maxIter=15, regParam=0.01, implicitPrefs=True)
    # model = als.fit(train)

    cvEstimator = CrossValidator(estimator=alsImplicit, estimatorParamMaps=paramMapImplicit, evaluator=evaluator)

    cvModel = cvEstimator.fit(train)

    return cvModel, evaluator


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

    (cvModel, evaluator) = recommendation(training)

    spark.stop()
