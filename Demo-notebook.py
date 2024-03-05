# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC Select "hello world from sql"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1

# COMMAND ----------

##Title2 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Title 2 

# COMMAND ----------

# MAGIC %fs ls '/'

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

display(files)

# COMMAND ----------


