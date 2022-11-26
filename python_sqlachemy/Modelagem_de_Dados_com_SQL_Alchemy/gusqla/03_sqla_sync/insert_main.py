
from conf.db_session import craete_session
from model.aditivo_nutritivo import AditivoNutritivo
from model.tipo_embalagem import TipoEmbalagem
from model.sabor import Sabor





# 1-AditivoNutritivo
def insert_aditivo_nutritivo():
    """
    The insert_aditivo_nutritivo function inserts a new Aditivo Nutritivo into the database.
    It requires no input and returns nothing.

    :return: :
    :doc-author: Trelent
    """
    print('Cadastrando Aditivo Nutritivo')

    nome= input('Informe o nome do Aditivo Nutritivo:')

    formula_quimita=input('Informe a fórmula química do Aditivo Nutritivo:')

    an =AditivoNutritivo(nome=nome,formula_quimita=formula_quimita)

    with craete_session() as session:
            session.add(an)
            session.commit()


    print('Aditivo Nutritivo cadastrado com sucesso!')
    print(f'ID: {an.id}')
    print(f'Data de Criação: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Formula Quimica: {an.formula_quimica}')

# 2- Sabor
def insert_sabor():
    """
        The insert_sabor function inserts a new Sabor object into the database.
        It requires no parameters and returns no values.

        :return: :
        :doc-author: Trelent
    """

    print('Cadastrando Sabor')

    nome = input('Informe o sabor do picole:')

    sb = Sabor(nome=nome)

    with craete_session() as session:
        session.add(sb)
        session.commit()


    print('Sabor cadastrado com sucesso!')
    print(f'ID: {sb.id}')
    print(f'Data de Criação: {sb.data_criacao}')
    print(f'Nome: {sb.nome}')

# 3- tipo de embalagem
def insert_tipo_embalagem():
    """
    The insert_tipo_embalagem function inserts a new tipo_embalagem into the database.


    :return: The id of the inserted item
    :doc-author: Trelent
    """

    print('Cadastrando Tipo de Embalagem')

    nome = input('Informe o Tipo de Embalagem:')

    temb = TipoEmbalagem(nome=nome)

    with craete_session() as session:
        session.add(temb)
        session.commit()

    print('Tipo de Embalagem cadastrado com sucesso!')
    print(f'ID: {temb.id}')
    print(f'Data de Criação: {temb.data_criacao}')
    print(f'Nome: {temb.nome}')



if __name__=="__main__":
    # 1
    insert_aditivo_nutritivo()
    # 2
    insert_sabor()
    # 3
    insert_tipo_embalagem()
