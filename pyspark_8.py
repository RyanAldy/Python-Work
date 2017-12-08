from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.types import *

def records(rec):
    return (int(rec[0]), rec[3], int(rec[9]))

def split_string(a):
    Data = a.split(",")
    return Data

c = SparkConf()
sc = SparkContext(conf = c)
sql = SQLContext(sc)

RDD = sc.textFile("/Ryan_spark/SALES.csv")
First = RDD.first()
RDD2 = RDD.filter(lambda x: x <> First)
RDD3 = RDD2.map(split_string)
RDD4 = RDD3.filter(lambda x: x[6] != '')
RDD5 = RDD4.map(records)

DF = sql.createDataFrame(RDD5, ["Year", "Product", "Quantity"])
DF2 = DF.filter((DF.Year >= 2004) & (DF.Year <= 2007))
DF3 = DF.sort(DF.Year.asc())
DF3.groupBy(DF.Year).sum("Quantity").show()
