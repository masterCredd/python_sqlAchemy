from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import String
from datetime import datetime
from conf.db_session import ModelBase


class TipoPicole(ModelBase):

    __tablename__ = 'tipos_picole'

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    data_criacao = Column(
        DateTime,
        default=datetime.now,
        index=True
    )
    nome = Column(
        String(45),
        unique=True,
        nullable=False
    )

    def __repr__(self) -> str:
        """
        The __repr__ function is what defines the string representation of an object.
        It's called by the repr() built-in function and by string conversions (reverse quotes).
        The __repr__ method is used for developer debugging and logging, not meant to be read by humans.
        If you want a human readable explanation of your object, define a __str__ method.

        :param self: Access the attributes and methods of the class
        :return: The string representation of the object
        :doc-author: Trelent
        """
        return f'<Tipo Picole: {self.nome}>'
