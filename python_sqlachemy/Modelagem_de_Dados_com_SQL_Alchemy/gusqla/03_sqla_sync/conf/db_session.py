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
        The createEngine function creates a SQLAlchemy engine object.
        It is used to create connections to the database.
        The function takes one argument, sql, which defaults to False.
        If sql is set to True then an SQLite database will be created in
        the db folder and a connection string for that database will be returned.

        :param sql:bool=False: Determine whether to use sqlite or postgresql
        :return: The engine object
        :doc-author: Trelent
    """
    global __async_engine

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
        con_str = f'sqlite+aiosqlite:///{arquivo_db}'
        __async_engine = create_async_engine(
            url=con_str,
            echo=False,
            connect_args={"check_same_thread": False}
        )
    else:
        # Postgres
        ...


def create_session():
    """
        The craete_session function creates a new SQLAlchemy session.
        It is used to create a singleton instance of the Session class,
        which can be reused by multiple classes.
        The function takes no arguments and returns an instance of the Session class.

        :return: A session object that is bound to the engine
        :doc-author: Trelent
    """
    ...


def create_tables():
    """
        The create_tables function creates all the tables in the database.


        :return: The modelbase
        :doc-author: Trelent
    """
    ...
