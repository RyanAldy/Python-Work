from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.types import *

def split_string(a):
    Data = a.split(",")
    return Data


c = SparkConf()
sc = SparkContext(conf = c)
sqlC = SQLContext(sc)

RDD1 = sc.textFile("/Ryan_spark/data.csv")
RDD2 = RDD1.map(split_string)

schema = StructType([
    StructField("regno", StringType(), True),
    StructField("name", StringType(), True),
    StructField("Mark", LongType(), False)])

DF = sql.createDataFrame(RDD2, schema)
DF2 = DF.registerTempTable("MarksData")

DF3 = sqlC.sql("select * from MarksData")
