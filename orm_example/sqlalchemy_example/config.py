import os

# PostgreSQL (docker compose up -d in the parent folder)
# "postgresql+psycopg://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>"
POSTGRES_URI = "postgresql+psycopg://{user}:{password}@localhost:{port}/shop_sqlalchemy".format(
    user=os.getenv("POSTGRES_USER", "shop"),
    password=os.getenv("POSTGRES_PASSWORD", "shop"),
    port=os.getenv("POSTGRES_PORT", "5433"),
)

# SQLite
# "sqlite:///<DATABASE_PATH>" or "sqlite:///:memory:"
SQLITE_URI = "sqlite:///shop.db"

# set DATABASE_URI=sqlite to run without docker
DATABASE_URI = SQLITE_URI if os.getenv("DATABASE_URI") == "sqlite" else POSTGRES_URI
