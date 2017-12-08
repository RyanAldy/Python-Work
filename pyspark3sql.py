# Movie with Highest Average rating for Western movies
from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.types import *


def split_string(a):
    Data = a.split(",")
    return Data

def convert_movie_fields(rec):
    return (int(rec[0]), rec[1], rec[2])

def convert_ratings_fields(rec):
    return(int(rec[0]), int(rec[1]), float(rec[2]), rec[3])

c = SparkConf()
sc = SparkContext(conf = c)
sqlC = SQLContext(sc)

moviesRDD = sc.textFile("/Ryan_spark/moviesnew.csv")
moviesRDD2 = moviesRDD.map(split_string)
moviesRDD3 = moviesRDD2.map(convert_movie_fields)

ratingsRDD = sc.textFile("/Ryan_spark/ratings.csv")
ratingsRDD2 = ratingsRDD.map(split_string)
ratingsRDD3 = ratingsRDD2.map(convert_ratings_fields)

movies_header = ["movieid", "title", "genres"]
ratings_header = ["userid", "movieid", "rating", "timestamp"]

moviesDF = sqlC.createDataFrame(moviesRDD3, movies_header)
moviesDF2 = moviesDF.registerTempTable("MovieData")

ratingsDF = sqlC.createDataFrame(ratingsRDD3, ratings_header)
ratingsDF2 = ratingsDF.registerTempTable("RatingsData")

#westernavgdf = sqlC.sql("select avg(a.rating) as avgrating from RatingsData a, MovieData b where a.movieid = b.movieid and b.genres like '%Western%'").show()
westernavgdf = sqlC.sql("select b.title, avg(a.rating) as avgrating from RatingsData a, MovieData b where a.movieid = b.movieid and b.genres like '%Western%' group by b.title")
max_row = westernavgdf.rdd.max(lambda row: row.avgrating)
print max_row.title
