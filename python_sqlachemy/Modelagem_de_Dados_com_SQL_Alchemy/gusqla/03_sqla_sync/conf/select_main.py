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
    """
        The select_todos_aditivos_nutritivos function prints out all of the aditivos_nutritivos in the database.


        :return: A list of objects containing all the aditivonutritivo
        :doc-author: Trelent
    """
    with create_session() as session:
        # tipo 1
        adnv=session.query(AditivoNutritivo)
        # tipo 2
        adv2=session.query(AditivoNutritivo).all()


        for adn in adnv:
            print(f'ID: {adn.id} ')
            print(f'Data de Criação: {formata_data(adn.data_criacao)} ')
            print(f'Nome: {adn.nome} ')
            print(f'Formula Quimica: {adn.formula_quimica} ')


# 2 --> SELECT * FROM sabores WHERE sabores.id==id_sabor
def select_filter_sabor(id_sabor:int):
    """
        The select_filter_sabor function accepts an id_sabor parameter and returns the Sabor object with that id. If no sabor has that ID, it returns None.

        :param id_sabor:int: Specify the id of the sabor that we want to retrieve
        :return: The following:
        :doc-author: Trelent
    """
    with create_session() as session:
        # tipo 1
        # sb = session.query(Sabor).filter(Sabor.id==id_sabor).first()

        # tipo 2 (recomendado)

        sb_1 = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        # tipo 3
        # sb_1 = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        # tipo 4 first -> one_or_one -> one
        # sb_1 = session.query(Sabor).where(Sabor.id == id_sabor).one()

        if sb_1==None:
            print('o Sabor procurado não existe!')
        else:
            print(f'ID: {sb_1.id}')
            print(f'Data de Criação: {formata_data(sb_1.data_criacao)}')
            print(f'Nome: {sb_1.nome}')



# 3 --> SELECT * FROM picole
def setelec_complexo_picole():
    """
        The setelec_complexo_picole function prints out all the information about a picole.
        It takes no arguments.

        :return: :
        :doc-author: Trelent
    """
    with create_session() as session:
        pcl=session.query(Picole).all()

        for pc in pcl:
            print(f'ID: {pc.id}')
            print(f'Data de Criação: {formata_data(pc.data_criacao)}')
            print(f'Preço: R$ {pc.preco}')

            # dados do sabor
            print(f'Sabor ID: {pc.id_sabor}')
            print(f'Sabor: {pc.sabor.nome}')

            # dados da embalagem
            print(f'Embalagem ID:{pc.id_tipo_embalagem}')
            print(f'Embalagem :{pc.tipo_embalagem.nome}')

            # dados do tipo de picole
            print(f'Tipo de Picole ID: {pc.id_tipo_picole}')
            print(f'Tipo de Picole : {pc.tipo_picole.nome}')

            # dados dos ingredientes
            print(f'Ingredientes: {pc.ingredientes}')

            # dados dos aditivos nutritivos
            print(f'Aditivos Nutritivos:{pc.aditivos_nutritivos} ')

            # dodos dos conservantes
            print(f'Conservantes: {pc.conservantes}')


# 4 --> SELECT * FROM sabor order by ...
def select_ordem_sabor():
    """
        The select_ordem_sabor function prints out the ID, date created, and name of every Sabor.


        :return: The name of the flavor
        :doc-author: Trelent
    """
    with create_session() as session:
        sb_or_b=session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

        for sb_or in sb_or_b:
            print(f'ID: {sb_or.id}')
            print(f'Data de Criação: {formata_data(sb_or.data_criacao)}')
            print(f'Nome: {sb_or.nome}')




if __name__=="__main__":
    # 1
    select_todos_aditivos_nutritivos()

    # 2
    select_filter_sabor(12)

    # 3
    setelec_complexo_picole()

    # 4
    select_ordem_sabor()
