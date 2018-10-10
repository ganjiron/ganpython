from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Ch02").getOrCreate()
sc = spark.sparkContext
# print(sc)
#

# block_*.csv만 따로 모아놓은 디렉토리
rawblocks = sc.textFile("C:\ganseo\src\ganpython\jupyter\LargeScaleDataProcess\linkage_csv")
rawblocks

rawblocks.first()

if __name__ == '__main__':
    pass
