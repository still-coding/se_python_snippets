# Piccolo example

Docs: https://piccolo-orm.readthedocs.io/

Start PostgreSQL first (`docker compose up -d --wait` in the parent folder), then:

```sh
uv run create_data.py
uv run query.py
```

* `piccolo_conf.py` - database connection, found by Piccolo automatically
* `tables.py` - the models
* `create_data.py` - creates tables and fills them from `../static_data`
* `query.py` - joins, many-to-many, aggregation
