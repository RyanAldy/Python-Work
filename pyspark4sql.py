# Most popular film among teenage girls
# Find the movie with the highest count of 5 star ratings
from pyspark import SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.types import *


def split_string(a):
    Data = a.split(",")
    return Data

def split_users_string(a):
    Data = a.split("|")
    return Data

def convert_movie_fields(rec):
    return (int(rec[0]), rec[1], rec[2])

def convert_ratings_fields(rec):
    return(int(rec[0]), int(rec[1]), float(rec[2]), rec[3])

def convert_users_fields(rec):
    return(int(rec[0]), int(rec[1]),rec[2], rec[3], rec[4])

c = SparkConf()
sc = SparkContext(conf = c)
sqlC = SQLContext(sc)

moviesRDD = sc.textFile("/Ryan_spark/moviesnew.csv")
moviesRDD2 = moviesRDD.map(split_string)
moviesRDD3 = moviesRDD2.map(convert_movie_fields)

ratingsRDD = sc.textFile("/Ryan_spark/ratings.csv")
ratingsRDD2 = ratingsRDD.map(split_string)
ratingsRDD3 = ratingsRDD2.map(convert_ratings_fields)

usersRDD = sc.textFile("/Ryan_spark/u.user")
usersRDD2 = usersRDD.map(split_users_string)
usersRDD3 = usersRDD2.map(convert_users_fields)

movies_header = ["movieid", "title", "genres"]
ratings_header = ["userid", "movieid", "rating", "timestamp"]
users_header = ["userid", "age", "gender", "occupation", "postcode"]

moviesDF = sqlC.createDataFrame(moviesRDD3, movies_header)
moviesDF2 = moviesDF.registerTempTable("MovieData")

ratingsDF = sqlC.createDataFrame(ratingsRDD3, ratings_header)
ratingsDF2 = ratingsDF.registerTempTable("RatingsData")

usersDF = sqlC.createDataFrame(usersRDD3, users_header)
usersDF2 = usersDF.registerTempTable("userData")

topmovieiddf = sqlC.sql("select movieid, userid, count(*) as ratingcount from RatingsData where rating=5 group by movieid, userid order by userid asc, movieid asc")
topmovieiddf.registerTempTable("topmovieidtab")
idcount = sqlC.sql("select a.movieid, a.userid, a.ratingcount from topmovieidtab a, userData b where a.userid = b.userid and b.age between 13 and 19 and gender='F'")
idcount.registerTempTable("femaletab")
max_count = sqlC.sql("select movieid, sum(ratingcount) as ratingsum from femaletab group by movieid")
max_count.registerTempTable("MaxCountTab")
movie_name = sqlC.sql("select a.title, a.movieid, b.ratingsum from MovieData a, MaxCountTab b where a.movieid = b.movieid")
max_row = movie_name.rdd.max(lambda row: row.ratingsum)
print max_row.title
