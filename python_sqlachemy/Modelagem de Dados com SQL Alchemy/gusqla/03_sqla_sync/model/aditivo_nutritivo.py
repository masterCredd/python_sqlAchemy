from sqlalchemy import Column, BigInteger, DateTime, String
from datetime import datetime
from conf.db_session import ModelBase


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
        return f'<Aditivo Nutritivo:{self.nome}>'