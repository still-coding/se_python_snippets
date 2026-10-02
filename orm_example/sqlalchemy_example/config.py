import os

_user = os.getenv("POSTGRES_USER", "shop")
_password = os.getenv("POSTGRES_PASSWORD", "shop")
_port = os.getenv("POSTGRES_PORT", "5433")

# PostgreSQL (`docker compose up -d --wait` in the parent folder)
# "postgresql+psycopg://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>"
POSTGRES_URI = f"postgresql+psycopg://{_user}:{_password}@localhost:{_port}/shop_sqlalchemy"

# SQLite
# "sqlite:///<DATABASE_PATH>" or "sqlite:///:memory:"
SQLITE_URI = "sqlite:///shop.db"

# set DATABASE_URI=sqlite to run without docker
DATABASE_URI = SQLITE_URI if os.getenv("DATABASE_URI") == "sqlite" else POSTGRES_URI
