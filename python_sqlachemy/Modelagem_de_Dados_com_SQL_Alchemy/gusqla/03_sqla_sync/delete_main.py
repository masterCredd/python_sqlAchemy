
"""
    sumary_line
    1 --> Buscar o registro a ser deletado;
    2 --> Fazer a deleção do objeto encontrado;
    3 --> Registrar no banco de dados a deleção;
"""


from typing import Optional

from conf.db_session import create_session
from model.revendedor import Revendedor
from model.picole import Picole


# 1
def deletar_picole(id_picole: int):
    """
        The deletar_picole function deletes a picole from the database.
        It takes one argument, an integer representing the id of the picole to be deleted.
        If it finds a matching picole, it will delete that row from the database and return True.
        Otherwise, it returns False.

        :param id_picole:int: Identify the picole that will be deleted
        :return: None
        :doc-author: Trelent
    """
    with create_session() as session:
        p = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if p != None:
            session.delete(p)
            session.commit()
        else:
            print(f'O ID:{id_picole}  desse Picole não existe')

# 2


def select_revendedor_filter(id_rev: int):
    """
        The select_revendedor_filter function accepts an integer id_rev as input and returns the revendedor with that id.
        If no such revendedor is found, it prints a message to the user.

        :param id_rev:int: Filter the query by id
        :return: The information of a revendedor
        :doc-author: Trelent
    """
    with create_session() as session:
        r = session.query(Revendedor).filter(
            Revendedor.id == id_rev).one_or_none()

        if r != None:
            print(f'ID: {r.id}')
            print(f'Razão Social: {r.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com o ID: {id_rev}')

# 3


def delete_revendedor(id_r: int):
    """
        The delete_revendedor function deletes a revendedor from the database.
        It takes an integer id_r as its only argument and returns nothing.

        :param id_r:int: Identify the id of the revendedor that will be deleted
        :return: None
        :doc-author: Trelent
    """
    with create_session() as session:
        re = session.query(Revendedor).filter(
            Revendedor.id == id_r).one_or_none()

        if re != None:
            session.delete(re)
            session.commit()
        else:
            print(f'O ID: {id_r} do Revendedor informador não existe')


if __name__ == '__main__':

    from update_main import select_filter_picole
    # ___________________________________________________
    # 1
    id_p = 21

    # fazer a consulta antes de deletar
    select_filter_picole(id_picole=id_p)

    # deletando o picole
    deletar_picole(id_picole=id_p)
    # ___________________________________________________

    # 2
    # fazer a consulta antes de deletar
    id_reve = 22
    select_revendedor_filter(id_rev=id_reve)

    # deletar o Revendedor
    delete_revendedor(id_r=id_reve)
    # ___________________________________________________
