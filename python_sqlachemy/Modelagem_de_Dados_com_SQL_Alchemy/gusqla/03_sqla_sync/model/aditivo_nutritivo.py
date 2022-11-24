from datetime import datetime

from conf.db_session import ModelBase
from sqlalchemy import BigInteger, Column, DateTime, String


class AditivoNutritivo(ModelBase):

    __tablename__ = 'aditivos_nutritivos'

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
    formula_quimica = Column(
        String(45),
        unique=True,
        nullable=False
    )

    def __repr__(self) -> str:
        """
        The __repr__ function is what defines the string representation of an object.
        It's called by the repr() built-in function and by string conversions (reverse quotes).
        The __repr__ method is used to display data in a way that can be copied and pasted into code.

        :param self: Access the attributes and methods of the class
        :return: The string representation of the object
        :doc-author: Trelent
        """
        return f'<Aditivo Nutritivo:{self.nome}>'
