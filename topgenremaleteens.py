# Most popular genre among teenage males
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
    return(int(rec[0]), int(rec[1]), int(rec[2]), rec[3])

def convert_users_fields(rec):
    return(int(rec[0]), int(rec[1]),rec[2], rec[3], rec[4])

c = SparkConf()
sc = SparkContext(conf = c)
sqlC = SQLContext(sc)

moviesRDD = sc.textFile("/Ryan_spark/moviesnew.csv")
moviesRDD2 = moviesRDD.map(split_string)
moviesRDD3 = moviesRDD2.map(convert_movie_fields)

# movie.data is an amended version of ratings.csv
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
idcount = sqlC.sql("select a.movieid, a.userid, a.ratingcount from topmovieidtab a, userData b where a.userid = b.userid and b.age between 13 and 19 and b.gender='M'")
idcount.registerTempTable("maletab")
max_count = sqlC.sql("select movieid, sum(ratingcount) as ratingsum from maletab group by movieid")
max_count.registerTempTable("MaxCountTab")
popular_genre = sqlC.sql("select a.genres, a.movieid, b.ratingsum from MovieData a, MaxCountTab b where a.movieid = b.movieid")
#popular_genre.registerTempTable("NewMaxCountTab")
idcountlist = popular_genre.select("genres").rdd.flatMap(lambda x: x[0].split("|")).collect()
#print idcountlist

word_counter = {}
for word in idcountlist:
     if word in word_counter:
         word_counter[word] += 1
     else:
         word_counter[word] = 1

popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
print popular_words[:1]
#top_3 = popular_words[:3]
