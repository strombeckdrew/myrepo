from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_db_pipeline_100325.config.ConfigStore import *
from test_db_pipeline_100325.functions import *

def test_target_100325(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("`hive_metastore`.`pipelinehub`.`deploy_test`")
