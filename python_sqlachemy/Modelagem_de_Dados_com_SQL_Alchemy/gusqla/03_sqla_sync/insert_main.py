
from conf.db_session import craete_session
from model.aditivo_nutritivo import AditivoNutritivo
from model.conservante import Conservante
from model.ingrediente import Ingrediente
from model.lote import Lote
from model.nota_fiscal import NotaFiscal
from model.picole import Picole
from model.revendedor import Revendedor
from model.sabor import Sabor
from model.tipo_embalagem import TipoEmbalagem
from model.tipo_picole import TipoPicole


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


    # print('Aditivo Nutritivo cadastrado com sucesso!')
    # print(f'ID: {an.id}')
    # print(f'Data de Criação: {an.data_criacao}')
    # print(f'Nome: {an.nome}')
    # print(f'Formula Quimica: {an.formula_quimica}')
    return an





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

# 4- tipo de Picole

def insert_tipo_picole():
    """
        The insert_tipo_picole function inserts a new TipoPicole into the database.
        It requires no parameters and returns nothing.

        :return: :
        :doc-author: Trelent
    """


    print('Cadastrando Tipo de Picole')

    nome = input('Informe o Tipo de Picole:')

    tip = TipoPicole(nome=nome)

    with craete_session() as session:
        session.add(tip)
        session.commit()

    print('Tipo de Picole cadastrado com sucesso!')
    print(f'ID: {tip.id}')
    print(f'Data de Criação: {tip.data_criacao}')
    print(f'Nome: {tip.nome}')

# 5- Ingredientes


def insert_ingrediente():
    """
        The insert_ingrediente function inserts a new Ingrediente into the database.
        It requires no parameters and returns nothing.

        :return: :
        :doc-author: Trelent
    """

    print('Cadastrando ingrediente')

    nome = input('Informe o ingrediente:')

    ingred = Ingrediente(nome=nome)

    with craete_session() as session:
        session.add(ingred)
        session.commit()

    # print('Ingrediente cadastrado com sucesso!')
    # print(f'ID: {ingred.id}')
    # print(f'Data de Criação: {ingred.data_criacao}')
    # print(f'Nome: {ingred.nome}')

    return ingred

# 6- Conservante


def insert_conservante():
    """
        The insert_conservante function inserts a new conservante into the database.
        It requires no parameters and returns nothing.

        :return: :
        :doc-author: Trelent
    """

    print('Cadastrando conservante')

    nome = input('Informe o conservante:')

    descricao= input('Informe a descrição do conservante')

    conserv = Conservante(nome=nome,descricao=descricao)

    with craete_session() as session:
        session.add(conserv)
        session.commit()

    # print('Conservante cadastrado com sucesso!')
    # print(f'ID: {conserv.id}')
    # print(f'Data de Criação: {conserv.data_criacao}')
    # print(f'Nome: {conserv.nome}')
    # print(f'Descrição:{conserv.descricao}')

    return conserv

# 7- Revendedor


def insert_revendedor():
    """
        The insert_revendedor function inserts a new revendedor into the database.

        :return: The object revend
        :doc-author: Trelent
    """


    print('Cadastrando revendedor')

    cnpj = input('Informe o cnpj do Revendedor:')

    razao_social = input('Informe a razão social do Revendedor')

    contato = input('Informe o contato do Revendedor')

    revend = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with craete_session() as session:
        session.add(revend)
        session.commit()

    return revend

# 8- lote


def insert_lote():
    """
        The insert_lote function inserts a new lote into the database.

        :return: The object lt
        :doc-author: Trelent
    """

    print('Cadastrando lote')


    id_tp_picole= input('Informe o id do picole')

    quantidade = input('Informe a quantidade do lote:')

    lt = Lote(id_tipo_picole=id_tp_picole, quantidade=quantidade)

    with craete_session() as session:
        session.add(lt)
        session.commit()

    return lt


# 9- nota fiscal


def insert_nota_fiscal():
    """
        The insert_nota fiscal function inserts a new nota fiscal into the database.

        :return: The object lt
        :doc-author: Trelent
    """

    print('Cadastrando a nota fiscal')

    valor = input('Informe o valor da Nota Fiscal')

    num_serie = input('Informe numero de serie da Nota Fiscal:')

    descricao= input('Informe a descrição da Nota Fiscal')

    id_revd = input('Informe o código do Revendedor')

    ntfisc = NotaFiscal(
        valor=valor,
        numero_serie=num_serie,
        descricao=descricao,
        id_revendedor=id_revd)

    lt_01=insert_lote()
    ntfisc.lotes.append(lt_01)

    lt_02 = insert_lote()
    ntfisc.lotes.append(lt_02)

    revd=insert_revendedor()
    id_revd=revd.id

    with craete_session() as session:
        session.add(ntfisc)
        session.commit()

    print('Nota Fiscal cadastrada com sucesso!')
    print(f'ID: {ntfisc.id}')
    print(f'Data: {ntfisc.data_criacao}')
    print(f'Valor: {ntfisc.valor}')
    print(f'Numero de Serie: {ntfisc.numero_serie}')
    print(f'descrição: {ntfisc.descricao}')
    print(f'ID do Revendedor: {ntfisc.id_revd}')
    print(f'Revendedor: {ntfisc.revendedor.razao_social}')


# 10- picole


def insert_picole():
    """
        The insert_picole function inserts a new picole into the database.

        :return: The object lt
        :doc-author: Trelent
    """

    print('Cadastrando o picole')

    preco = input('Informe o preço do Picole:')

    tp_embalagem=input('Informe o ID do Tipo da Embalagem:')

    sab = input('Informe o ID do Sabor :')

    tp_picole = input('Informe o ID do Tipo de Picole:')

    id_revd = input('Informe o código do Revendedor')

    picole = Picole(
        id_sabor=sab,
        id_tipo_embalagem=tp_embalagem,
        id_tipo_picole=tp_picole,
        preco=preco
    )

    ingred_01=insert_ingrediente()
    picole.ingredientes.append(ingred_01)

    ingred_02 = insert_ingrediente()
    picole.ingredientes.append(ingred_02)



    conprov_01=insert_conservante()

    picole.conservantes.append(conprov_01)

    nutri_01=insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(nutri_01)



    with craete_session() as session:
        session.add(picole)
        session.commit()

    print('Picole cadastrada com sucesso!')
    print(f'ID: {picole.id}')
    print(f'Data: {picole.data_criacao}')
    print(f'Preço: {picole.preco}')
    print(f'Sabor: {picole.sabor.nome}')
    print(f'Tipo Picole: {picole.tipo_picole.nome}')
    print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}')
    print(f'Ingredientes: {picole.ingredientes}')
    print(f'Conservantes: {picole.conservantes}')
    print(f'Aditivos Nutritivos : {picole.aditivos_nutritivos}')



def inserir_dados():
    """
        The inserir_dados function inserts data into the database.


        :return: :
        :doc-author: Trelent
        """
    # 1
    insert_aditivo_nutritivo()
    # 2
    insert_sabor()
    # 3
    insert_tipo_embalagem()

    # 4
    insert_tipo_picole()

    # 5
    insert_ingrediente()

    # 6
    insert_conservante()

    # 7
    rev = insert_revendedor()
    print(f'ID: {rev.id}')
    print(f'Data de Criação: {rev.data_criacao}')
    print(f'CNPJ: {rev.cnpj}')
    print(f'Razão social: {rev.razao_social}')
    print(f'Contato: {rev.Contato}')

    # 8
    lti = insert_lote()
    print(f'ID: {lti.id}')
    print(f'Data de Criação: {lti.data_criacao}')
    print(f'ID tipo de picole: {lti.id_tipo_picole}')
    print(f'Razão social: {lti.quantidade}')
    print(f'Contato: {rev.Contato}')

    # 9
    insert_nota_fiscal()

    # 10
    insert_picole()




if __name__=="__main__":
    inserir_dados()
