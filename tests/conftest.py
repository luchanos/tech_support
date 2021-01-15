import pytest
import asyncpg
from subprocess import PIPE, Popen
import os

DB_ORDERS_TEST = "postgres://postgres:dbpass@0.0.0.0:5432/db"


@pytest.fixture()
async def db_pool():
    db_pool = await asyncpg.create_pool(DB_ORDERS_TEST)
    yield db_pool
    await db_pool.close()


def run_migrations(migrations_path):
    cmd = f"yoyo apply --database {DB_ORDERS_TEST} {migrations_path} -b"
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode:
        raise Exception(f"Error during run migrations! {stderr} due to execution command '{cmd}'")


def execute_sql_query(command):
    cmd = f"psql -U postgres -h 0.0.0.0 -p 5432 -c '{command}' db"
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, env=dict(os.environ, PGPASSWORD="dbpass"))
    stdout, stderr = process.communicate()
    if process.returncode:
        raise Exception(f"Error during run sql query! {stderr} due to execution command '{cmd}'")


@pytest.fixture(autouse=True, scope='session')
def create_test_database():
    execute_sql_query(
        """
        DROP SCHEMA IF EXISTS public CASCADE;
        CREATE SCHEMA IF NOT EXISTS public;
        GRANT USAGE ON SCHEMA public to PUBLIC;
        GRANT CREATE ON SCHEMA public to PUBLIC;
    """
    )
    run_migrations("./orders_db/migrations")


TABLES = ['orders', ]


@pytest.fixture(autouse=True, scope='function')
async def clean_tables(db_pool):
    cleaner_sql = """TRUNCATE TABLE %s"""

    for table in TABLES:
        await db_pool.fetch(cleaner_sql % (table, ))

    yield

    for table in TABLES:
        await db_pool.fetch(cleaner_sql % (table, ))
