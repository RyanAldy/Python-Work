from pyspark import SparkContext, SparkConf

def records(rec):
    Data = rec.split(",")
    amount = int(Data[6]) * int(Data[7])
    return (Data[1], amount)


c = SparkConf()
sc = SparkContext(conf = c)

RDD = sc.textfile("/Ryan_spark/SALES.csv")
First = RDD.first()

RDD2 = RDD.filter(lambda x: x <> First)
RDD3 = RDD2.map(records)
Data = RDD4.collect()
