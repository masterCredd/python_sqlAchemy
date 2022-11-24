from datetime import datetime
from typing import List, Optional

from conf.db_session import ModelBase
from model.aditivo_nutritivo import AditivoNutritivo
from model.conservante import Conservante
from model.ingrediente import Ingrediente
from model.sabor import Sabor
from model.tipo_embalagem import TipoEmbalagem
from model.tipo_picole import TipoPicole
from sqlalchemy import (DECIMAL, BigInteger, Column, DateTime, ForeignKey,
                        Integer, Table)
from sqlalchemy.orm import relationship

ingredientes_picoles = Table(
    'ingredientes_picole',
    ModelBase.metadata,
    Column(
        'id_picole',
        Integer,
        ForeignKey('picoles.id')
    ),
    Column(
        'id_ingrediente',
        Integer,
        ForeignKey('ingredientes.id')
    )
)

conservantes_picole = Table(
    'conservantes_picole',
    ModelBase.metadata,
    Column(
        'id_picole',
        Integer,
        ForeignKey('picoles.id')
    ),
    Column(
        'id_conservante',
        Integer,
        ForeignKey('conservantes.id')
    )
)

aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    Column(
        'id_picole',
        Integer,
        ForeignKey('picoles.id')
    ),
    Column(
        'id_aditivo_nutritivo',
        Integer,
        ForeignKey('aditivos_nutritivos.id')
    )
)


class Picole(ModelBase):

    __tablename__ = 'picoles'

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
    preco = Column(
        DECIMAL(8, 2),
        nullable=False
    )
    id_sabor = Column(
        Integer,
        ForeignKey('sabores.id')
    )
    sabor = relationship(
        'Sabor',
        lazy='joined'
    )
    id_tipo_embalagem = Column(
        Integer,
        ForeignKey('tipos_embalagem.id')
    )

    tipo_embalagem: TipoEmbalagem = relationship(
        'TipoEmbalagem',
        lazy='joined'
    )

    id_tipo_picole = Column(
        Integer,
        ForeignKey('tipos_picole.id')
    )

    tipo_picole: TipoPicole = relationship(
        'Tipopicole',
        lazy='joined'
    )

    # ingredientes: List[Ingrediente]
    ingredientes: List[Ingrediente] = relationship(
        'Ingrediente',
        secondary=ingredientes_picoles,
        backref='ingrediente',
        lazy='joined'
    )

    # conservantes: Optional[List[Conservantes]]
    # conservantes
    conservantes: Optional[List[Conservante]] = relationship(
        'Conservante',
        secondary=conservantes_picole,
        backref='conservante',
        lazy='joined'
    )

    # aditivos_nutritivos: Optional[List[AditivosNutritivos]]
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = relationship(
        'AditivoNutritivo',
        secondary=aditivos_nutritivos_picole,
        backref='aditivo_nutritivo',
        lazy='joined'
    )

    def __repr__(self) -> str:
        """
        The __repr__ function is what defines the string representation of the object.
        It's called by default when you try to &quot;print&quot; an object, or convert it to a string.
        :param self: Refer to the object itself
        :return: A string that represents the object
        :doc-author: Trelent
        """

        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
