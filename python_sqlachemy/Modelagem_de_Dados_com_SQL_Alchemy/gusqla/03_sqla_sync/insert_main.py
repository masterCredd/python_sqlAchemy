
from conf.db_session import craete_session
from model.aditivo_nutritivo import AditivoNutritivo

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
            print('Erro de inserção de dados')

    print('Aditivo Nutritivo cadastrado com sucesso!')
    print(f'ID: {an.id}')
    print(f'Data de Criação: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Formula Quimica: {an.formula_quimica}')

if __name__=="__main__":
    insert_aditivo_nutritivo()
