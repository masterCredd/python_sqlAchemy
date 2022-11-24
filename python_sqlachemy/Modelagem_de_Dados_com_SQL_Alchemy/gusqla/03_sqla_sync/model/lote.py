from datetime import datetime

from conf.db_session import ModelBase
from model.tipo_picole import TipoPicole
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Lote(ModelBase):

    __tablename__ = 'lotes'

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
    id_tipo_picole = Column(
        Integer,
        ForeignKey('tipos_picole.id')
    )
    tipo_picole = relationship(
        'TipoPicole',
        lazy='joined'
    )
    quantidade = Column(
        Integer,
        nullable=False
    )

    def __repr__(self):
        """
        The __repr__ function is meant to be an unambiguous representation of an object and should be used for debugging and logging,
        as well as inter-process communication (used by the pickle serialization module).
        The __str__ function is meant to be more of a readable repesentation of an object and is meant to be used as a display to the end-user.

        :param self: Refer to the object itself
        :return: A string representation of the object
        :doc-author: Trelent
        """

        return f'<Lote: {self.id}>'
