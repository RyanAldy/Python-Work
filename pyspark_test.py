# Run it with spark-submit rather than pyspark + filename
from pyspark import SparkContext, SparkConf

def double_element(x):
    return(x * 2)

def even_odd(x):
    if (x % 2 == 0):
        return(x , "even")
    else:
        return(x , "odd")

def reduce_example(A, B):
    return(A + B)

def filter_numbers(X):
    return(x > 4)

# RDD means Resilient Distrubuted Dataset
# Reduce is an action - always returns values, list, value etc
# Map is a transformation - returns a RDD

List1 = [1,2,3,4,5,6]
c = SparkConf()
sc = SparkContext(conf = c)
RDD1 = sc.parallelize(List1)
RDD2 = RDD1.map(even_odd)
RDD3 = RDD1.reduce(reduce_example)
Data = RDD2.collect()
print Data
print RDD3

RDD4 = RDD1.map(double_element).filter(filter_numbers).reduce(reduce_example)
print RDD4

#.filter(lambda x: x % 2 == 0)

Trainers = ["Shafeeq", "Ryan", "Adam", "Kris", "Shafeeq"]
Trainees = ["Shafeeq", "Joe", "John", "James", "Jack"]

Trainers_RDD = sc.parallelize(Trainers)
Trainees_RDD = sc.parallelize(Trainees)

RDD1 = Trainers_RDD.distinct()
data1 = RDD1.collect()
print data1

RDD2 = Trainers_RDD.union(Trainees_RDD)
data2 = RDD2.collect()
print data2

RDD3 = Trainers_RDD.intersection(Trainees_RDD)
data3 = RDD3.collect()
print data3

RDD4 = Trainers_RDD.subtract(Trainees_RDD)
data4 = RDD4.collect()
print data4
