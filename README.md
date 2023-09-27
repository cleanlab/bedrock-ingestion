# Bedrock

Scaffolding and example code for a simple app (API only, no UI). Includes:

- A Flask app with `/ping` endpoint
- A Postgres database

## Development tips

- This repo uses [Docker Compose](https://docs.docker.com/compose/). Get the
  site running locally with `docker compose up --build`. Test that it's working
  by navigating to <http://localhost:8080/ping>.
- The Flask web server is set up to auto-reload on changes
- To interact with the service, use a REST client like
  [Postman](https://www.postman.com/product/rest-client/), or use cURL on your
  command line.

## Example interaction

```console
$ curl localhost:8080/ping
{
  "message": "Ping!"
}
```

## Warm-up exercise

If you want an idea for a warm-up exercise to get familiar with modifying the
code here are some ideas:

- Add a `/view` endpoint that returns a JSON of the first 100 entries of an
  arbitrary Postgres table (ignoring the safety implications of this...)
  - This should get you more comfortable with using Flask + SQLAlchemy
  - Might even come in handy during the interview itself!
  - When the app initializes, it will create a `dummy_data` table in Postgres
    with the following contents
    | foo | bar    | baz    |
    |-----|--------|--------|
    | 1   | "bar1" | "blah" |
    | 2   | "bar2" | "halb" |
