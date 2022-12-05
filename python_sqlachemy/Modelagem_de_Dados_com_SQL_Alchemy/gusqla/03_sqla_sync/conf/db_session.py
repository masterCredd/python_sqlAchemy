from pathlib import Path
from typing import Optional

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()


# __engine: Optional[Engine] = None
__async_engine: Optional[AsyncEngine] = None


def createEngine(sql: bool = False):
    """
        The createEngine function creates a global async engine object that is used by all the other functions in this module.
        It uses the create_async_engine function from SQLAlchemy to do so.
        The function takes one argument, sql, which defaults to False and indicates whether or not we are using Postgresql or SQLite.

        :param sql:bool=False: Indicate whether the connection is to be made with sqlite or postgres
        :return: The engine created
        :doc-author: Trelent
    """

    global __async_engine

    # dados de acesso postgres
    user = 'postgres'
    password = 'postgres'
    bd = 'picoles'
    port = '5441'

    if __async_engine != None:
        return

    if sql:
        # SQLite
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(
            parents=True,
            exist_ok=True
        )
        conn_str = f'sqlite+aiosqlite:///{arquivo_db}'
        __async_engine = create_async_engine(
            url=conn_str,
            echo=False,
            connect_args={"check_same_thread": False}
        )
    else:
        # Postgres
        conn_str = f'postgres+asyncpg://{user}:{password}@localhost:{port}/{bd}'
        __async_engine = create_async_engine(
            url=conn_str,
            echo=False
        )
    return __async_engine


def create_session():
    """
        The craete_session function creates a new SQLAlchemy session.
        It is used to create a singleton instance of the Session class,
        which can be reused by multiple classes.
        The function takes no arguments and returns an instance of the Session class.

        :return: A session object that is bound to the engine
        :doc-author: Trelent
    """

    global __async_engine

    if not __async_engine:
        return createEngine()

    __async_session = sessionmaker(
        __async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    session = __async_session

    return session


async def create_tables():
    """
        The create_tables function creates all tables in the database.
        It is intended to be called once, when initializing the application.


        :return: A future object
        :doc-author: Trelent
    """

    global __async_engine

    if not __async_engine:
        return create_async_engine()

    import model.__all_models

    async with __async_engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
        await conn.run_sync(ModelBase.metadata.create_all)
