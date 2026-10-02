# ORM examples

A shop (customers, products, tags, orders and order details) implemented with SQLAlchemy 2.0:

* [`sqlalchemy_example`](sqlalchemy_example)

Data for it lives in [`static_data`](static_data) (generated with https://www.mockaroo.com/).

## PostgreSQL

```sh
docker compose up -d --wait   # creates the database shop_sqlalchemy
docker compose down -v        # stop and remove the data
```

Defaults: user `shop`, password `shop`, port `5433`. Override them with env variables
or a `.env` file (see `.env.example`).

## Run

```sh
cd sqlalchemy_example
uv run create_data.py   # drop/create tables and fill them
uv run query.py
```

It can also run on SQLite without docker: `DATABASE_URI=sqlite uv run create_data.py`.

## Checks

```sh
uv run ruff check . && uv run ruff format --check . && uv run pyright .
```
