# ORM examples

The same shop (customers, products, tags, orders and order details) implemented with two ORMs:

* [`sqlalchemy_example`](sqlalchemy_example) - SQLAlchemy 2.0, sync
* [`piccolo_example`](piccolo_example) - Piccolo, async

Both read the same data from [`static_data`](static_data) (generated with https://www.mockaroo.com/).

## PostgreSQL

```sh
docker compose up -d --wait   # creates databases shop_sqlalchemy and shop_piccolo
docker compose down -v        # stop and remove the data
```

Defaults: user `shop`, password `shop`, port `5433`. Override them with env variables
or a `.env` file (see `.env.example`).

## Run

```sh
cd sqlalchemy_example   # or piccolo_example
uv run create_data.py   # drop/create tables and fill them
uv run query.py
```

`sqlalchemy_example` can also run on SQLite without docker: `DATABASE_URI=sqlite uv run create_data.py`.

## SQLAlchemy vs Piccolo

| | SQLAlchemy | Piccolo |
|---|---|---|
| Style | sync (async is a separate setup) | async first, `.run_sync()` available |
| Models | `Mapped[...]` + `relationship()` | columns only, joins by `Order.customer.name` |
| Many-to-many | association `Table` + `relationship(secondary=...)` | joining table + `M2M(...)`, `add_m2m()` |
| Composite primary key | yes (`OrderDetails`) | no, a surrogate `id` is used |
| Arithmetic inside `Sum()` | yes | no, `raw()` is used for order totals |
| Schema changes | Alembic | built-in migrations (not used here) |
