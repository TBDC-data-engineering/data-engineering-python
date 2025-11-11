from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os


def main():
    # Set environment variables
    os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@17"
    os.environ["SPARK_HOME"] = "/Users/silvionormeygomez/Documents/apps/spark-4.0.0-bin-hadoop3"

    # Initialize SparkSession with Delta
    spark = SparkSession.builder \
        .appName("DeltaTableExample") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.connect.extensions.relation.classes","org.apache.spark.sql.connect.delta.DeltaRelationPlugin") \
        .config("spark.connect.extensions.command.classes", "org.apache.spark.sql.connect.delta.DeltaCommandPlugin") \
        .getOrCreate()



    # Create a simple DataFrame with some data
    data = [
        ("RIDE_1", "V1", "2024-01-01", "2024-01-02", 1, 2, 2, 5.5, 25.0),
        ("RIDE_2", "V1", "2024-01-02", "2024-01-03", 3, 4, 1, 8.0, 35.0)
    ]

    # Define the schema
    schema = StructType([
        StructField("RideId", StringType(), True),
        StructField("VendorId", StringType(), True),
        StructField("PickupTime", StringType(), True),
        StructField("DropTime", StringType(), True),
        StructField("PickupLocationId", IntegerType(), True),
        StructField("DropLocationId", IntegerType(), True),
        StructField("PassengerCount", IntegerType(), True),
        StructField("TripDistance", DoubleType(), True),
        StructField("TotalAmount", DoubleType(), True)
    ])

    # Create DataFrame
    df = spark.createDataFrame(data, schema)

    # Write to Delta table
    delta_table_path = "./data/streaming/delta_table"

    # Ensure directory exists
    os.makedirs(os.path.dirname(delta_table_path), exist_ok=True)

    # Write initial data
    df.write.format("delta").mode("overwrite").save(delta_table_path)

    # Now read from Delta table
    delta_df = spark.read.format("delta").load(delta_table_path)

    # Show the contents
    print("Contents of Delta table:")
    delta_df.show()

    # Clean up
    spark.stop()


if __name__ == '__main__':
    main()