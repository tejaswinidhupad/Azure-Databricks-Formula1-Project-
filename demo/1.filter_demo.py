# Databricks notebook source
# MAGIC %run "../includes/configuration"

# COMMAND ----------

races_df = spark.read.parquet(f"{processed_folder_path}/races")

# COMMAND ----------

races_filter_df1 = races_df.filter("race_year = 2019 AND round <= 5")

# COMMAND ----------

display(races_filter_df1)

# COMMAND ----------

races_filter_df2 = races_df.filter((races_df.race_year == 2020) & (races_df.round <= 5))

# COMMAND ----------

display(races_filter_df2)
