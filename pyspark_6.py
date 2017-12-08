from pyspark import SparkContext, SparkConf
from pyspark.sql import *

def split_string(a):
    Data = a.split(",")
    return Data


c = SparkConf()
sc = SparkContext(conf = c)
sql = SQLContext(sc)

RDD1 = sc.textFile("/Ryan_spark/data.csv")
#schema = StructType
RDD2 = RDD1.map(split_string)
DF = sql.createDataFrame(RDD2)
DF.filter(DF._3 > 50).select(DF._1.alias("Reg No"), DF._2.alias("Name"), (DF._3*100/150).alias("Perc")).show()
