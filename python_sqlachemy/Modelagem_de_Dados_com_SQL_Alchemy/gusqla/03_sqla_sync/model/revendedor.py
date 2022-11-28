from datetime import datetime

from conf.db_session import ModelBase
from sqlalchemy import BigInteger, Column, DateTime, String


class Revendedor(ModelBase):

    __tablename__ = 'revendedor'

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

    cnpj = Column(
        String(45),
        unique=True,
        nullable=False
    )

    razao_social = Column(
        String(100),
        nullable=False
    )

    contato = Column(
        String(100),
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
        return f'<Revendedor: {self.cnpj}>'
