### Json transformer example

Here is a simple example of json transformer that changes list of objects.

#### Resources

* [example.py](example.py) - Python transformer that applies transformation rules
* [config.yaml](config.yaml) - Greenmask configuration file that uses the transformer
* [data.txt](data.txt) - Input data file for testing purposes
* [docker-compose.yaml](docker-compose.yml) - Docker compose file to run Greenmask playground with the transformer
  that can be used for testing and development
* [Dockerfile](Dockerfile) - Dockerfile to build the transformer image with python environment
* [schema.sql](schema.sql) - SQL file to create a sample table in the database for testing purposes

#### Input data and transformation rules

Here we have a JSON data that contains array of item. It's required to transform each item in the array.:

```json
[
  {
    "id": 1,
    "item": "notebook",
    "price": 233.9
  },
  {
    "id": 2,
    "item": "lamp",
    "price": 430.79
  }
]
```

The rules:
* Add 1000 to each "id" if id attribute exists
* Change "item" value to that can be choosen from ranom list
    ```
    "keyboard",
    "mouse",
    "monitor",
    "printer",
    "desk",
    "chair",
    "lamp",
    "notebook",
    "pen",
    "headphones",
   ```
* Generate a random price between 10.0 and 500.0

### How to run a test with data

Use a command below to run a test with data from the example above:

```bash
cat data.txt | python3 example.py
```

### Run in playground

Run docker compose playground to see the transformer in action:

```shell
docker compose run greenmask
```

Once in the container you can run validate command:

```shell
greenmask --config config.yaml validate --data --diff --rows-limit=4 --format=vertical
```

The resul t should be similar to:

```text
+-----------+--------+--------------------------------+--------------------------------+
| %LineNum% | Column | OriginalValue                  | TransformedValue               |
+-----------+--------+--------------------------------+--------------------------------+
| 0         | id     | 1                              | 1                              |
+           +--------+--------------------------------+--------------------------------+
|           | data   | [{"id": 1, "item": "keyboard", | [{"id": 1001, "item":          |
|           |        | "price": 49.99}, {"id": 2,     | "headphones", "price":         |
|           |        | "item": "mouse", "price":      | 400.92}, {"id": 1002, "item":  |
|           |        | 19.99}]                        | "chair", "price": 367.96}]     |
+-----------+--------+--------------------------------+--------------------------------+

```

To execute the transformation use the command below inside the container:

```shell
greenmask --confi


If you want to connect to database:

```shell
docker compose exec -it playground-db psql -U postgres -d postgres
```


