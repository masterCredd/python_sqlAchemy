"""
    sumary_line
    1 -> Buscar o registro a ser atualizado;
    2 -> Faz as alterações no registro;
    3 -> Salva o registro no banco de dados;
"""

from conf.db_session import create_session
from model.sabor import Sabor
from model.picole import Picole
from conf.helpers import formata_data

# 1


def atualizar_sabor(id_sabor: int, novo_nome: str):
    """
        The atualizar_sabor function updates the name of a given sabor.
        It takes two parameters: id_sabor and novo_nome.
        If the sabor exists, it will update its name to novo_nome.

        :param id_sabor:int: Identify the sabor that will be updated
        :param novo_nome:str: Set the new name of the flavor
        :return: None
        :doc-author: Trelent
    """
    with create_session() as session:
        sb = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sb != None:
            sb.nome = novo_nome
            session.commit()

        else:
            print(f' Não existe o sabor com ID {id_sabor}')

# 2.1


def select_filter_picole(id_picole: int):
    """
        The select_filter_picole function allows the user to select a picole by ID and display its information.

        :param id_picole:int: Identify the picole to be selected
        :return: A picole object
        :doc-author: Trelent
    """
    with create_session() as session:
        p = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if p != None:
            print(f'ID: {p.id}')
            print(f'Sabor: {p.Sabor.nome}')
        else:
            print(f'O ID {id_picole} buscado não existe.')


# 2.2


def atualizar_picole(id_picole, novo_preco: float, novo_sabor: int):
    """
        The atualizar_picole function updates the price of a picole.

        :param id_picole: Identify the picole that will be updated
        :param novo_preco:float: Update the price of a picole
        :param novo_sabor:int: Set the new sabor of the picole
        :return: None
        :doc-author: Trelent
    """
    with create_session() as session:
        pat = session.query(Picole).filter(
            Picole.id == id_picole).one_or_none()

        if pat != None:
            pat.preco = novo_preco

            if novo_sabor != None:
                pat.id_sabor = novo_sabor

            session.commit()
        else:
            print(f' Não existe o Picole com ID {id_picole}')


if __name__ == '__main__':

    from select_main import select_filter_sabor

    # 1
    # ______________________________________________
    # consultar antes
    id_s = 42
    select_filter_sabor(id_sabor=id_s)

    # 1- atualizar
    atualizar_sabor(
        id_sabor=id_s,
        novo_nome='Abacate'
    )

    # consultar novamente
    select_filter_sabor(id_sabor=id_s)
    # ______________________________________________

    # 2.1
    # ______________________________________________
    # consultar antes

    id_p = 21
    novo_p = 9.99
    id_s = 42

    select_filter_picole(id_picole=id_p)

    # 2.2 - atualizar
    atualizar_picole(
        id_picole=id_p,
        novo_preco=novo_p,
        novo_sabor=id_s
    )

    # consultar novamente
    select_filter_picole(id_picole=id_p)
    # ______________________________________________
