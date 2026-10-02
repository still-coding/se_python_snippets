# SQLAlchemy example

Part of [orm_example](../README.md): see it for how to start PostgreSQL.

* `models.py` - declarative models (`Mapped[...]`, composite primary key in `OrderDetails`,
  many-to-many through `products_tags`); `uv run models.py` prints the `CREATE TABLE` for `Product`
* `tools.py` - engine and session factory
* `create_data.py` - creates tables and fills them from `../static_data`
* `query.py` - joins, aggregation, relationships

Data generated with https://www.mockaroo.com/
