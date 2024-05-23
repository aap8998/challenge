## Challenge Backend

Welcome to Ariel's code challenge, featuring a FastAPI backend for serving a csv file via GraphQL

### How to run

docker compose up --build

this demo will show up in localhost:8000

### Endpoints

/graphql 

This endpoint serves the items from our parsed csv

Can be accessed from a browser too, for a nice testing UI


/nlp

Here we can text a natural language query string service, wich is mocked


/docs

Swagger service for documentation
