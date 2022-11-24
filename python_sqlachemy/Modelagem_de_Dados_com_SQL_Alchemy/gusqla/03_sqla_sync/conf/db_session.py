from pathlib import Path
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

ModelBase = declarative_base()


# __engine: Optional[Engine] = None
__engine = None


def createEngine(sql: bool = False):
    """
    The createEngine function creates a SQLAlchemy engine object.
    It is used to create connections to the database.
    The function takes one argument, sql, which defaults to False.
    If sql is set to True then an SQLite database will be created in the db folder and a connection string for that database will be returned.

    :param sql:bool=False: Determine whether to use sqlite or postgresql
    :return: The engine object
    :doc-author: Trelent
    """

    global __engine

    type_db = 'postgresql'
    user = 'postgres'
    port = '5441'
    database = 'picoles'
    local = 'localhost'
    password = 'postgres'

    if __engine:
        return

    if sql:
        file_db = 'db\\picoles.sqlite'
        folder = Path(file_db).parent
        folder.mkdir(
            parents=True,
            exist_ok=True
        )
        conn_str = f'sqlite:///{file_db}'
        __engine = create_engine(
            url=conn_str,
            echo=False,
            connect_args={"check_same_thread": False}
        )
    else:
        conn_str = f'{type_db}://{user}:{password}@{local}:{port}/{database}'
        __engine = create_engine(
            url=conn_str,
            echo=False
        )
    return __engine


def craete_session():
    """
        The craete_session function creates a new SQLAlchemy session.
        It is used to create a singleton instance of the Session class, which can be reused by multiple classes.
        The function takes no arguments and returns an instance of the Session class.

        :return: A session object that is bound to the engine
    :doc-author: Trelent
    """
    global __engine

    if not __engine:
        createEngine(sql=True)
        # createEngine()
    __session = sessionmaker(
        __engine,
        expire_on_commit=False,
        class_=Session
    )

    session: Session = __session()

    return session


def create_tables():
    """
    The create_tables function creates all the tables in the database.


    :return: The modelbase
    :doc-author: Trelent
    """
    global __engine

    if not __engine:
        createEngine(sql=True)
        # createEngine()

    import model.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
