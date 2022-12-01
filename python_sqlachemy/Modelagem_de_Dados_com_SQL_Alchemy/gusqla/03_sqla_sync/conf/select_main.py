from typing import List
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session
from model.aditivo_nutritivo import AditivoNutritivo
from model.sabor import Sabor
from model.revendedor import Revendedor
from model.picole import Picole



# 1  --> SELECT * FROM aditivos_nutritivos;
def select_todos_aditivos_nutritivos():
    with create_session() as session:
        adnv=session.query(AditivoNutritivo)

        for adn in adnv:
            print(f'ID: {adn.id} ')
            print(f'Data de Criação: {formata_data(adn.data_criacao)} ')
            print(f'Nome: {adn.nome} ')
            print(f'Formula Quimica: {adn.formula_quimica} ')



if __name__=="__main__":
    # 1
    select_todos_aditivos_nutritivos()
