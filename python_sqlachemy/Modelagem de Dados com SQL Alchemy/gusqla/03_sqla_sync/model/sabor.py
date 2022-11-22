from sqlalchemy import Column, BigInteger, DateTime, String
from datetime import datetime
from conf.db_session import ModelBase


class Sabor(ModelBase):

    __tablename__ = 'sabores'

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
        The __repr__ function is what defines the string representation of the object.
        It's called by default when a string representation of the object is needed, such as
        when it gets passed to print(). It should always return a string.

        :param self: Refer to the object itself
        :return: The string representation of the object
        :doc-author: Trelent
        """
        return f'<Sabores: {self.nome}>'
