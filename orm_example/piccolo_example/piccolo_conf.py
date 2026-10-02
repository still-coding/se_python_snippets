import os

from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

# Piccolo finds this file by itself: it is imported as module `piccolo_conf`
# (run scripts from this folder or set PICCOLO_CONF).
DB = PostgresEngine(
    config={
        "database": "shop_piccolo",
        "user": os.getenv("POSTGRES_USER", "shop"),
        "password": os.getenv("POSTGRES_PASSWORD", "shop"),
        "host": "localhost",
        "port": int(os.getenv("POSTGRES_PORT", "5433")),
    }
)

# Tables are created from code (see create_data.py), so no apps are registered.
# In a real project you would register an app here and use migrations.
APP_REGISTRY = AppRegistry(apps=[])
