# pyspark-notebooks

A collection of PySpark notebooks created in Databricks to practise data transformation, cleaning, and basic ETL workflows.

## Contents
- PySpark data cleaning
- Data transformation examples
- Simple ETL notebook workflows

## Tools
- Databricks Free Edition
- PySpark
- GitHub

## Goal
This repository is part of my learning and portfolio development in data engineering.

### Bronze Baby Names Transformation Notebook
This notebook demonstrates core PySpark concepts using a Bronze layer dataset:

🔹 Transformations
Narrow transformations (filter, withColumn, drop, rename)
Wide transformations (groupBy aggregation)

🔹 Actions
count()
show()
collect()

🔹 Dataset Schema
name (string)
sex (string)
count (int)
source_file (string)

🔹 Learning Goals
Understand Spark execution model
Practice ETL transformation steps
Demonstrate Bronze → Silver pipeline concepts

### Banking Data Pipeline (CSV → Bronze → Silver → Gold)
This project demonstrates an end-to-end data engineering pipeline using Databricks, implementing the Medallion Architecture (Bronze, Silver, Gold).


🔹Data ingestion from CSV files (Unity Catalog volumes)

🔹Data transformation using PySpark

🔹JOIN operations across multiple datasets

🔹Data modelling and relational integration

🔹Aggregations for business-ready insights
