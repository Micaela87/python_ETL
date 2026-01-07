## Description
ETL real-time flow with CDC integration

This ptoject aims to create a system that captures CRUD operations (insert, update, delete) on a MongoDb collection and uses the data collected to perform other operations and at the same time consumes it for analytics purposes

## Technologies
Python 3.10.0
Pyspark 4.0.1
MongoDb with replicaSet
RabbitMQ
Docker

## Workflow
CDC mechanism wathces for changes on MongoDb [users] collection and sends messages to an [events] queue in RabbitMQ. Messages in [events] queue are consumed by ETLService, which is responsible for extracting data from MongoDb [events] collection, manipulate them to transform them in a Pyspark DataFrame and save results in MongoDb [analytics] collection for analytics purposes.

The CDC mechanism has been build on top of .watch() method, available only on databases with replicaSet enabled.

MongoDb [events] collection has been designed to accept an [action] field (for webhooks purposes) and a [callback] field to execute callbacks when changes are captured. In this way, additional actions and scripts could be executed when CRUD operations are performed on a collection, considering webhoocks could reach other servers in a cluster/distributed system

## Project Setup
```bash
$ docker compose up
$ pip install -r requirements.txt
$ python main.py
```