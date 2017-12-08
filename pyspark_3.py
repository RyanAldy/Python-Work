from pyspark import SparkContext, SparkConf

def records(rec):
    column9 = float(rec[8])
    column10 = float(rec[9])
    return (column9 * column10)

def split_string(a):
    Data = a.split(",")
    return Data

c = SparkConf()
sc = SparkContext(conf = c)

RDD = sc.textFile("/Ryan_spark/SALES.csv")
First = RDD.first()

RDD2 = RDD.filter(lambda x: x <> First)
RDDa = RDD2.map(split_string)
RDD3 = RDDa.filter(lambda x: x[8] != '')
RDD4 = RDD3.map(records)
Data = RDD4.collect()
print Data
