# Find the movie with the highest count of 5 star ratings
from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.types import *


def split_string(a):
    Data = a.split(",")
    return Data

def split_tab_string(a):
    Data = a.split("\t")
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

ratingsRDD = sc.textFile("/Ryan_spark/movie.data")
ratingsRDD2 = ratingsRDD.map(split_tab_string)
ratingsRDD3 = ratingsRDD2.map(convert_ratings_fields)

movies_header = ["movieid", "title", "genres"]
ratings_header = ["userid", "movieid", "rating", "timestamp"]

moviesDF = sqlC.createDataFrame(moviesRDD3, movies_header)
moviesDF2 = moviesDF.registerTempTable("MovieData")

ratingsDF = sqlC.createDataFrame(ratingsRDD3, ratings_header)
ratingsDF2 = ratingsDF.registerTempTable("RatingsData")

#moviesDF3 = sqlC.sql("select title from MovieData where movieid in (select movieid from RatingsData where movieid = (select max(count(*)) from RatingsData where rating = 5 group by movieid))").show()

topmovieiddf = sqlC.sql("select movieid, count(*) as ratingcount from RatingsData where rating=5 group by movieid")
topmovieiddf.registerTempTable("topmovieidtab")
maxidcount = sqlC.sql("select a.title, a.movieid, b.ratingcount from MovieData a, topmovieidtab b where a.movieid = b.movieid order by ratingcount desc")
maxidcount.registerTempTable("maxidtab")
maxnum = sqlC.sql("select max(ratingcount) as maxrating from maxidtab")
topresult = maxnum.first().maxrating
# Use .format to use variable in SQL query
topmovie = sqlC.sql("select title from maxidtab where ratingcount = {0}".format(topresult)).show()
