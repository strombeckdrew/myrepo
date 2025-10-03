from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_db_pipeline_100325.config.ConfigStore import *
from test_db_pipeline_100325.functions import *

def test_dataset_100325(spark: SparkSession) -> DataFrame:
    return spark.read.table("`hive_metastore`.`pipelinehub`.`nimbustest_table`")
