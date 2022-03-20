# OpenScience Framework (OSF) Extract-Transform-Load (ETL) Pipeline and API

This repository hosts an OpenSource API capable of performing ETL processes upon data files in certain formats from the OpenScience Framework API.

In its first iteration, it will be able to ingest .bdf files into a MongoDB document store from which endpoints will expose this data in JSON format.
Such data will be publically available through any exposed endpoints and then presented on a future web-app.

The principal web technology leveraged here is FastAPI. The motivation being to make use of the many data science toolkits within Python in order to manipulate the ingested data
and to contribute to the OpenAPI initiative by creating a transparent and free data source.

Spinning up the server is as simple as installing [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) on your OS and running
the command at the directory root: `docker-compose up`
