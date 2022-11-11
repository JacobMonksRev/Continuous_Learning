import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, explode

spark = SparkSession\
    .builder\
    .appName("Pyspark Test")\
    .master("local[*]")\
    .getOrCreate()

sc = spark.sparkContext

def my_filter(x):
    if x > 5:
        return True
    else:
        return False


# rdd_numbers = sc.parallelize(range(10))
# print("Now printing the RDD data...")
# print(rdd_numbers.collect())

# rdd_filtered = rdd_numbers.filter(my_filter)
# print("Now printing the RDD data...")
# print(rdd_filtered.collect())

# rdd_squared = rdd_numbers.map(lambda x: x**2)
# print("Now printing the RDD data...")
# print(rdd_squared.collect())

rdd_values = sc.parallelize([(1,'Jacob',40),(2,'Bob',21),(3,'Maria',33)])
df_values = rdd_values.toDF()
df_labeled = df_values.withColumnRenamed('_1','id')
df_labeled = df_labeled.withColumnRenamed('_2','name')
df_labeled = df_labeled.withColumnRenamed('_3','age')
print("Now printing the Dataframe data...")
df_labeled.show()
df_updated = df_labeled.withColumn('age',when(col('age') == 40, lit(80)).when(col('age') == 21, lit(21)).when(col('age') == 33, lit(33)))
print("Now printing the Dataframe data...")
df_updated.show()
df_newcolumn = df_updated.withColumn('legal_status',when(col('age') >= 65,lit('senior citizen')).otherwise(lit('citizen')))
print("Now printing the Dataframe data...")
# df_newcolumn.show()

df_newcolumn.createTempView('people')

df_queried = spark.sql("SELECT legal_status, COUNT(legal_status) FROM people GROUP BY legal_status")

# df_raw = spark.read.json('Python/sample.json',multiLine='true')
# df_raw.show()
# df_renamed = df_raw.withColumnRenamed('id','key')
# df_columns = df_renamed.select('key','batters.batter')
# df_columns.show()

# df_exploded = df_columns.select('key',explode('batter').alias('flavors'))
# df_exploded.select(df_exploded.flavors.type).show()