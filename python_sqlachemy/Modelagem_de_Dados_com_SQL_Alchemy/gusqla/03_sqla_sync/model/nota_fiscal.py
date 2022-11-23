from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import DECIMAL
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from model.revendedor import Revendedor
from model.lote import Lote
from conf.db_session import ModelBase
from typing import List


lotes_nota_fiscal = Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    Column(
        'id_nota_fiscal',
        Integer,
        ForeignKey('notas_fiscais.id')
    ),
    Column(
        'id_lote',
        Integer,
        ForeignKey('lotes.id'),
    )

)


class NotaFiscal(ModelBase):

    __tablename__ = 'notas_fiscais'

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
    valor = Column(
        DECIMAL(8, 2),
        nullable=False
    )
    numero_serie = Column(
        String(45),
        unique=True,
        nullable=False
    )
    descricao = Column(
        String(200),
        nullable=False
    )
    id_revendodor = Column(
        Integer,
        ForeignKey('revendedor.id'),

    )
    revendedor: Revendedor = relationship(
        'Revendedor',
        lazy='joined'
    )

    # lotes:List[Lote]
    lotes: List[Lote] = relationship(
        'Lote',
        secondary=lotes_nota_fiscal,
        backref='lote',
        lazy='dynamic'
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

        return f'<Nota Fiscal: {self.numero_serie}>'