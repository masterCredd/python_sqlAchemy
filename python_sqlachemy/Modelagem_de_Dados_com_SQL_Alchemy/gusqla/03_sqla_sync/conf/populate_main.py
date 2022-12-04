import asyncio

from tqdm import tqdm  # pip install tqdm
from sqlalchemy.ext.asyncio import AsyncSession

from conf.helpers import gerar_string, gerar_int, gerar_float, gerar_cor
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


#1) Aditivos Nutritivos
async def populate_aditivo_nutritivo():
    print(f'Cadastrando Aditivo Nutritivo: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
    
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()
        formula_quimica: str = gerar_string(frase=True)

        aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
        session.add(aditivo_nutritivo)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Aditivos Nutritivos cadastrados com sucesso')

#2) Sabores
async def populate_sabor():
    print(f'Cadastrando Sabores: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()

        sabor: Sabor = Sabor(nome=nome)
        session.add(sabor)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Sabores cadastrados com sucesso')

#3) Tipos Embalagem
async def populate_tipo_embalagem():
    print(f'Cadastrando Tipos Embalagem: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()

        tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)
        session.add(tipo_embalagem)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Tipos Embalagem cadastrados com sucesso')


#4) Tipos Picole
async def populate_tipo_picole():
    print(f'Cadastrando Tipos Picolé: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()

        tipo_picole: TipoPicole = TipoPicole(nome=nome)
        session.add(tipo_picole)
        await asyncio.sleep(0.05)  
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Tipos Picolé cadastrados com sucesso')


#5) Ingredientes
async def populate_ingrediente():
    print(f'Cadastrando Ingredientes: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()

        ingrediente: Ingrediente = Ingrediente(nome=nome)
        session.add(ingrediente)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Ingredientes cadastrados com sucesso')

#6) Conservantes
async def populate_conservante():
    print(f'Cadastrando Conservantes: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
    
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        nome: str = gerar_string()
        descricao: str = gerar_string(frase=True)

        conservante: Conservante = Conservante(nome=nome, descricao=descricao)
        session.add(conservante)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Conservantes cadastrados com sucesso')


#7) Revendedor
async def populate_revendedor():
    print(f'Cadastrando Revendedores: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        cnpj: str = gerar_string()
        razao_social: str = gerar_string()
        contato: str = gerar_string()

        revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
        session.add(revendedor)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Revendedores cadastrados com sucesso')

#8) Lote
async def populate_lote():
    print(f'Cadastrando Lotes: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
    
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        id_tipo_picole: int = gerar_int()
        quantidade: int = gerar_int()

        lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
        session.add(lote)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Lotes cadastrados com sucesso')


#9) Nota Fiscal
async def populate_nota_fiscal():
    print(f'Cadastrando Notas Fiscais: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        valor: float = gerar_float(digitos=3)
        numero_serie: str = gerar_string()
        descricao: str = gerar_string(frase=True)
        id_revendedor: int = gerar_int()

        nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
        session.add(nota_fiscal)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Notas Fiscais cadastradas com sucesso')


#10) Piole
async def populate_picole():
    print(f'Cadastrando Picolés: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    session: AsyncSession = create_session()
        
    cor = gerar_cor()
    for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
        preco: float = gerar_float()
        id_sabor: int = gerar_int()
        id_tipo_embalagem: int = gerar_int()
        id_tipo_picole: int = gerar_int()

        picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
        
        # Ingredientes
        for n in range(5):
            nome: str = gerar_string()
            ingrediente: Ingrediente = Ingrediente(nome=nome)
            picole.ingredientes.append(ingrediente)

        op = gerar_float()
        if op > 5:
            for _ in range(3):
                # Aditivos Nutritivos
                nome: str = gerar_string()
                formula_quimica: str = gerar_string(frase=True)
                aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
                picole.aditivos_nutritivos.append(aditivo_nutritivo)
        else:
            for _ in range(3):
                # Conservantes
                nome: str = gerar_string()
                descricao: str = gerar_string(frase=True)
                conservante: Conservante = Conservante(nome=nome, descricao=descricao)
                picole.conservantes.append(conservante)
        session.add(picole)
        await asyncio.sleep(0.05)
    # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
    await session.commit()
    await session.close()
    print('Picolés cadastrados com sucesso')


async def popular():
    #1) Aditivos Nutritivos
    await populate_aditivo_nutritivo()

    #2) Sabores
    await populate_sabor()

    #3) Tipos Embalagem
    await populate_tipo_embalagem()

    #4) Tipos Picole
    await populate_tipo_picole()

    #5) Ingredientes
    await populate_ingrediente()

    #6) Conservantes (Deixando vazio para poder verificar resultados em tabelas vazias)
    # await populate_conservante()
    
    #7) Revendedores
    await populate_revendedor()

    #8) Lotes
    await populate_lote()

    #9) Notas Fiscais
    await populate_nota_fiscal()

    #10) Picole
    await populate_picole()


if __name__ == '__main__':
   asyncio.run(popular())
