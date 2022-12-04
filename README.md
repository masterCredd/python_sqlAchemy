
# SQL Alchemy: Essencial _Curso  🍧

---
🔜 🎓  **Introduction**

---

  Explica se faz a utilização do framework em uma aplicação real

---

🔜 🛠️   **Tools**

---
🔜  **[Tecnologias usadas no curso]**

⟹    [![Alt text](/img/terminal.png)](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=pt-br&gl=br "Terminal Windows")

⟹    [![Alt text](/img/visual_studio_code.png)](https://code.visualstudio.com/ "Visual Studio Code")

 ⟹   [![texto alt](/img/docker.png)](https://www.docker.com/products/docker-desktop/ "Docker")

⟹    [![Alt text](/img/python.png)](https://hub.docker.com/_/python/ "Python")

⟹    [![Alt text](/img/sqlachemy.png)](https://www.sqlalchemy.org/)

⟹    [![Alt text](/img/postogres.png)](https://www.postgresql.org "PostgreSQL")

⟹    [![Alt text](/img/SQLite.png)](https://www.sqlite.org/ "SQLite")

⟹    [![Alt text](/img/dbeaver.png)](https://dbeaver.io "DBeaver")

---

## Configurar o ambiente do python na ultima versão

    utilizando o **terminal** digite o seguinte
    📝 `comando:`

    ```bash
  -> docker pull python
    ```

* confirmar a versão instalada

     📝`comando:`

    ````bash

  -> python --version
    ````

* ✔️ Resposta:

    ````bash
  -->  Python 3.11.0
    ````

* ###  Instalar os pacotes necessários para fazer a aula

  ````bash
  --> pip install --require-hashes -r requirements.txt
  ````

* create engine docker bd postgres
  📝`comando:`

  ````bash
  -->  docker-composer up -d
  ````

---

🔜  ✅  **Sessão: 1️⃣ - Apresentação** [PARTE -1](https://github.com/masterCredd/python_sqlAchemy/tree/master/python_sqlachemy/Introdução_ao_SQL_Alchemy)

---
 ✅ 1. Sobre o curso

![Alt text](/python_sqlachemy/Apresenta%C3%A7%C3%A3o/sql_alchemy_v3.png)

 ✅ 2. Como conseguimos te ajudar

---

🔜  ✅ **Sessão: 2️⃣ - Introdução ao SQL Alchemy** [PARTE -2](https://github.com/masterCredd/python_sqlAchemy/tree/master/python_sqlachemy/Modelagem_de_Dados_com_SQL_Alchemy)

---

✅ 3. O que vamos aprender nesta seção?

✅ 4. Introdução ao SQLAlchemy :clipboard:[PDF](https://github.com/masterCredd/python_sqlAchemy/blob/master/python_sqlachemy/Introdução%20ao%20SQL%20Alchemy/02-introducao-ao-sqlalchemy.pdf)

✅ 5. Casos de sucesso do SQLAlchemy :clipboard: [PDF](https://github.com/masterCredd/python_sqlAchemy/blob/master/python_sqlachemy/Introdução%20ao%20SQL%20Alchemy/03-casos-de-sucesso-do-sqlalchemy.pdf)

✅ 6. Entendendo a Arquitetura do SQLAlchemy [PDF](https://github.com/masterCredd/python_sqlAchemy/blob/master/python_sqlachemy/Introdução%20ao%20SQL%20Alchemy/04-entendendo-a-arquitetura-do-sqlalchemy.pdf)

✅ 7. Recapturando

---

🔜   ✅ **Sessão: 3️⃣ - Modelagem de Dados com SQLAlchemy** [PARTE -3](https://github.com/masterCredd/python_sqlAchemy/tree/master/python_sqlachemy/Modelagem_de_Dados_com_SQL_Alchemy)

---

✅ 8. O que vamos aprender nesta seção?

![image](/python_sqlachemy/Modelagem_de_Dados_com_SQL_Alchemy/01.2+-+fabrica_picoles_ordenado.png "Diagrama Ilustrativo")

✅ 9.  Prática: Criando a Estrutura do Projeto - **Parte 1**

✅ 10. Prática: Criando a Estrutura do Projeto - **Parte 2**

✅ 11. Prática: Criando a Models - **Parte 1**

👉  **Exemplo para Criar uma Classe do Model**

  ```python
  #🐍

  class Sabor(ModelBase):

      __tablename__ = 'sabores'

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

      def __repr__(self) -> str:
          """
          The __repr__ function is what defines the string representation of the object.
          It's called by default when a string
          representation of the object is needed, such as
          when it gets passed to print(). It should always return a string.

          :param self: Refer to the object itself
          :return: The string representation of the object
          :doc-author: Trelent
          """
          return f'<Sabores: {self.nome}>'

  ```

✅ 12. Prática: Criando a Models - **Parte 2**

✅ 13. Prática: Criando a Models - **Parte 3**

✅ 14. Prática: Criando as tabelas no banco de dados

![image](/python_sqlachemy/Modelagem_de_Dados_com_SQL_Alchemy/gusqla/03_sqla_sync/picoles.sqlite.png)

✅ 15. Recapturando

---

🔜 🔲**Sessão: 4️⃣  - Manipulando Dados com SQLAlchemy**

---

✅ 16. O que vamos aprender nesta seção?

✅ 17. Entendendo o Padrão Unit of Work [PDF](https://github.com/masterCredd/python_sqlAchemy/blob/master/python_sqlachemy/Manipulando_Dados_com_SQL_Alchemy/02-entendendo-o-padrao-unit-of-work.pdf)

✅  18. Prática: Inserindo Dados - Create(`Insert`) - **Parte 1**

✅  19. Prática: Inserindo Dados - Create(`Insert`) - **Parte 2**

✅  20. Prática: Zerando e Populando o Banco de Dados

✅  21. Prática: Buscando Dados - Read(`Select`) - **Parte 1**

👉 **Exemplo de uma Função para selecionar todos os dados**

  ```python

  #🐍
    def select_todos_aditivos_nutritivos():
      """
          The select_todos_aditivos_nutritivos
          function prints out all of the aditivos_nutritivos in the database.

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
  ```

✅ 22. Prática: Buscando Dados - Read(`Select`) - **Parte 2**

 👉  **SQL Equivalents**

![image](/img/forma_de_filtros.png)

✅ 23. Compreendendo melhor relacionamentos

  ▶️  **Informações Adicionais**

🔜  🎀 Classes Python oferecem relacionamentos entre outras passes,
      mas estamos falando neste caso de orientação à objetos.
      Em banco de dados relacionais, temos refacimentos um-para-muitos e
      desta forma conseguimos resolver qualquer problema de normalização de
      dados aplicando as formas normais.

  👉 **Exemplo**

  ```python

  #🐍
    ...
    class Pais(ModelBase);

      __tablename__ = 'paises'

      id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
      )

      nome = Column(
        String(100),
        index=100,
        unique=True
      )

      cidades = List[Cidade]= relationship(
        'Cidade',
        back_populates='pais',
        lazy=True
      )
      ...

    class Cidade(ModelBase)

      __tablename__ = 'cidades'

      id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
      )

      nome = Column(
        String(100),
        index=100,
        unique=True
      )

      id_pais = Column(
        BigInteger,
        Foreinkey('paises.id')
      )

      pais = relationship(
        'Pais',
        back_populates='cidades'
      )
    ...
  ```

  🔜  🎀 A pate importante aqui é o parâmetro `lazy`, que neste exemplo está o com valor True

  🔜  🎀 Por padrão o parâmetro `lazy`,
  tem valor de `select`. Ou seja, mesmo que não especifiquemos este parâmetro, que é opcional, ele irá funcionar como `select`.
  Mas o que este `select` faz?

  🔜  🎀 O parâmetro `lazy`, determina como os objetos relacionados são "carregados" quando queridos pelos relacionamentos.

  🔜  🎀 Temos 4 principais valores para o parâmetro `Lazy`:

  📍 select(ou True);
  📍 dynamic;
  📍 joined(ou False);
  📍 subquery;

  🔜  🎀 Usando `Lazy` com o valor `'select'`(ou True)

  👉 **Exemplo**

  ```python

  #🐍
    ...
      cidades = List[Cidade]= relationship(
        'Cidade',
        back_populates='pais',
        lazy=True
      )
    ...
  ```

  🔜  🎀 Em relacionamento onde o campo relacionado faz uso de ``lazy='select'``,
  quando chamamos/carregamos o valor este emite/executa um comando ``SELECT`` trazendo todos os objetos relacionados.

  🔜  🎀 Por exemplo, se quisermos, através da consulta a um país,
    buscar todas as cidades relacionadas podemos fazer: ``session.query(Pais).fist().cidades``
    Desta forma teríamos uma lista de cidades deste país.

  🔜  🎀 Usando ``Lazy`` com o valor ``'dynamic'``:

  ```python

  #🐍
    ...
      cidades = List[Cidade]= relationship(
        'Cidade',
        back_populates='pais',
        lazy='dynamic'
      )
    ...
  ```

  🔜  🎀 Se realizarmos uma consulta igual a anterior mas de um model que possui
  um relacionamento usando ``lazy='dynamic'`` ao invés de termos uma lista de cidades,
  teríamos o comando ``Select`` por completo como saída, conforme: ``session.query(Pais).fist().cidades``

  ```SQL
  //⤵️
     SELECT paises.id AS pais_id paises.nome AS pais_nome FROM paises;
  ````

  🔜  🎀  Ou seja, desta forma temos um objeto SQLAlchemy ao invés da lista de cidades

  🔜  🎀 Porém, se executarmos a função ``all()``, ai sim teremos também nossa lista de cidades:

```python
...
session.query(Pais).first()cidades.all()
...
```

  🔜  🎀 O beneficio aqui é que podemos ir  além e adicionar filtros ou ordenar os dados conforme precisarmos.

  🔜  🎀 Usando ``Lazy`` com o valor ``'joined'`` (ou False)

```python

  #🐍
    ...
      cidades = List[Cidade]= relationship(
        'Cidade',
        back_populates='pais',
        lazy='joined'
      )
    ...
  ```

  🔜  🎀 Usando  ``lazy='joined'``, automaticamente é feito um join entre as duas tabelas e o resultado é retornado.

🔜  🎀 Usando ``Lazy`` com o valor ``'subquery'``

```python

  #🐍
    ...
      cidades = List[Cidade]= relationship(
        'Cidade',
        back_populates='pais',
        lazy='subquery'
      )
    ...
  ```

  🔜  🎀 Usando ``lazy='subquery'``, basicamente temos o mesmo resultado,
  exceto pelo fato de que subquery faz uso de subquery (Select dentro do select), enquanto joined faz uso de join.

  🔜  🎀 Mas por estarem em tabelas diferentes, o join sempre irá performar melhor.

✅ 24. Prática: Atualizando Dados - `Update`

* 🔲 25. Prática: Deletando Dados  - `Delete`
* 🔲 26. Recapturando

---

🔜 🔲**Sessão: 5️⃣ - SQLAlchemy Assíncrono**

---

* 🔲 27. O que vamos aprender nesta seção?
* 🔲 28. Revisando a Programação Assíncrona
* 🔲 29. Prática: Refaturando o Projeto
* 🔲 30. Prática: Refatorando o arquivo db_session.py
* 🔲 31. Prática: Refatorando o Insert
* 🔲 32. Prática: Refatorando Zerar a Base e Popular
* 🔲 33. Prática: Refatorando Select - **Parte 1**
* 🔲 34. Prática: Refatorando Select - **Parte 2**
* 🔲 35. Prática: Refatorando Update
* 🔲 36. Prática: Refatorando Delete
* 🔲 37. Recapturando

---

🔜 🔲**Sessão: 6️⃣ - (Extra) SQL Model**

---

* 🔲 38. O que vamos aprender nesta seção?
* 🔲 39. Introdução ao SQL Model **(PDF)**
* 🔲 40. Prática: Refatorando o Projeto
* 🔲 41. Prática: Refatorando os Models - **Parte 1**
* 🔲 42. Prática: Refatorando os Models - **Parte 2**
* 🔲 43. Prática: Refatorando o arquivo db_session.py
* 🔲 44. Prática: Refatorando o Insert
* 🔲 45. Prática: Refatorando Zerar a Base e Popular
* 🔲 46. Prática: Refatorando Select - **Parte 1**
* 🔲 47. Prática: Refatorando Select - **Parte 2**
* 🔲 48. Prática: Refatorando Update
* 🔲 49. Prática: Refatorando Delete
* 🔲 50. Recapturando

---

🔜 🔲**Sessão: 7️⃣ - (Extra) SQL Model Assíncrono**

---

* 🔲 51. O que vamos aprender nesta seção?
* 🔲 52. Prática: Refatorando o Projeto
* 🔲 53. Prática: Refatorando o arquivo db_session.py
* 🔲 54. Prática: Refatorando o Insert
* 🔲 55. Prática: Refatorando Zerar a Base e Popular
* 🔲 56. Prática: Refatorando Select - **Parte 1**
* 🔲 57. Prática: Refatorando Select - **Parte 2**
* 🔲 58. Prática: Refatorando Update
* 🔲 59. Prática: Refatorando Delete
* 🔲 60. Recapturando

---

🔜 🔲**Sessão: 8️⃣ - Encerramento**

---

* 🔲 61. Recapturando
* 🔲 62. Quais os Próximos passos
