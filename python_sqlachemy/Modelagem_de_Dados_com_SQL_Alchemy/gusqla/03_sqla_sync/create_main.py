from conf.db_session import create_tables
from asyncio import run

if __name__ == "__main__":
    run(create_tables())
