from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_db_pipeline_100325.config.ConfigStore import *
from test_db_pipeline_100325.functions import *
from prophecy.utils import *
from test_db_pipeline_100325.graph import *

def pipeline(spark: SparkSession) -> None:
    df_test_dataset_100325 = test_dataset_100325(spark)
    test_target_100325(spark, df_test_dataset_100325)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("test_db_pipeline_100325").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_db_pipeline_100325")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test_db_pipeline_100325", config = Config)(pipeline)

if __name__ == "__main__":
    main()
