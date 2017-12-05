# Script to sum the revenue for each country
from pyspark import SparkContext, SparkConf

def sum_revenue (x, y):
    return (x + y)

def records(rec):
    column6 = float(rec[5])
    column7 = float(rec[6])
    return (column6 * column7)

def split_string(a):
    Data = a.split(",")
    return Data

c = SparkConf()
sc = SparkContext(conf = c)

RDD = sc.textFile("/Ryan_spark/SALES.csv")
First = RDD.first()
RDD2 = RDD.filter(lambda x: x <> First)
RDD3 = RDD2.map(split_string)
RDD4 = RDD3.filter(lambda x: x[8] != '')
RDD5 = RDD4.map(records)

# Basically groups the values by key (Whatever this is in the dataset)
DATA1 = RDD5.countByKey()
# Groups it by country as that's what I returned as the first value into RDD5
DATA2 = RDD5.reduceByKey(sum_revenue)
#  Need to collect as its a transformation
finaldata = DATA2.collect()
DATA2.saveAsTextFile("/Ryan_spark/Revenuesum.csv")
print finaldata

# The file downloads in parts - so to merge and download to localhost:
# hadoop fs -getmerge /Ryan_spark/RevenueSum.csv/ /home/cloudera/Documents/revsum.csv
