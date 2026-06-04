# FranceWeatherAnalysis

## Overview

FranceWeatherAnalysis is a Data Engineering project designed to collect, process, store, and analyze weather data from French cities using a modern data pipeline architecture.

The project automates the extraction of weather information from a public API, stores raw data in a PostgreSQL database, performs large-scale data transformations using PySpark, and orchestrates the entire workflow with Apache Airflow.

The processed data is then made available for reporting and visualization tools such as Power BI.

This project demonstrates the implementation of an end-to-end ETL pipeline using industry-standard technologies commonly used in Data Engineering environments.

---

## Objectives

The main objectives of the project are:

* Automate the collection of weather data from multiple French cities.
* Store historical weather records in a relational database.
* Clean and transform raw data into analytics-ready datasets.
* Schedule and monitor workflows automatically.
* Produce datasets suitable for business intelligence and reporting.
* Demonstrate Data Engineering best practices.

---

## Architecture

```text
                Weather API
                     |
                     v
           Apache Airflow DAG
                     |
                     v
              PostgreSQL
               (Raw Data)
                     |
                     v
                 PySpark
             Data Processing
                     |
                     v
              PostgreSQL
           (Processed Data)
                     |
                     v
                 Power BI
```

---

## Technologies

### Programming

* Python

### Data Storage

* PostgreSQL

### Data Processing

* PySpark

### Workflow Orchestration

* Apache Airflow

### Containerization

* Docker

### Data Visualization

* Power BI

### Version Control

* Git
* GitHub

---

## Data Pipeline

### 1. Data Extraction

Weather data is collected from a public weather API at scheduled intervals.

Collected information includes:

* Temperature
* Humidity
* Atmospheric pressure
* Wind speed
* Weather conditions
* Timestamp
* City information

The extraction process is fully automated through Apache Airflow.

### 2. Raw Data Storage

The extracted data is stored in PostgreSQL without modification.

This layer serves as:

* Historical storage
* Data recovery source
* Audit and traceability layer

### 3. Data Transformation

PySpark is used to process and transform the raw weather data.

Transformation tasks include:

* Handling missing values
* Removing duplicates
* Standardizing formats
* Data validation
* Aggregation calculations
* Feature engineering

### 4. Processed Data Storage

The transformed datasets are stored in dedicated PostgreSQL tables optimized for analytics and reporting purposes.

Examples:

* Daily weather summaries
* Monthly statistics
* City comparisons
* Temperature trends

### 5. Reporting

The processed datasets can be connected directly to Power BI dashboards.

Example KPIs:

* Average temperature by city
* Rainfall trends
* Weather anomalies
* Monthly weather evolution
* Regional comparisons

---

## Project Structure

```text
FranceWeatherAnalysis/
│
├── airflow/
│   ├── dags/
│   └── logs/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── postgres/
│   └── init.sql
│
├── pyspark/
│   ├── transformations/
│   └── jobs/
│
├── dashboards/
│   └── powerbi/
│
├── docker/
│
├── tests/
│
├── requirements.txt
│
├── docker-compose.yml
│
└── README.md
```

---

## Features

* Automated weather data ingestion
* Scheduled ETL workflows
* Historical data storage
* Data quality checks
* Large-scale processing with PySpark
* Analytics-ready datasets
* Power BI integration
* Containerized deployment

---

## Data Engineering Concepts Demonstrated

This project demonstrates:

* ETL Pipeline Development
* Workflow Orchestration
* Data Modeling
* Relational Databases
* Data Transformation
* Data Quality Management
* Containerization
* Data Analytics Preparation
* Pipeline Automation

---

## Future Improvements

Potential future enhancements include:

* Real-time data ingestion using Apache Kafka
* Cloud deployment on Azure or AWS
* Data Lake integration
* Machine Learning forecasting models
* Advanced monitoring and alerting
* CI/CD pipeline implementation

---

## Author

**Omar Rahal**

Data Engineer / Data Analyst
