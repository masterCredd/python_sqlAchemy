from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from pathlib import Path
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base


ModelBase = declarative_base()


# __engine: Optional[Engine] = None
__engine = None


def createEngine(sql: bool = False):
    """sumary_line
    create string connection sqlite or postgresql
    Keyword arguments:
    argument -- description
    Return: __engine
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
    """sumary_line
        create session db
    Keyword arguments:
    argument -- description
    Return: session
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
    global __engine

    if not __engine:
        createEngine(sql=True)
        # createEngine()

    import model.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
