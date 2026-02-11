# Projeto: ETL Big Data Python
-----

## 📋 Sobre

Este projeto demonstra como processar eficientemente **1 bilhão de linhas de dados** (~14GB) usando diferentes abordagens em Python. O desafio é calcular estatísticas (mínimo, média e máximo) de temperaturas por estação meteorológica, comparando o desempenho de várias bibliotecas e técnicas.

[![Projeto](https://img.shields.io/badge/Projeto-Big%20Data-blue?style=for-the-badge)](https://suajornadadedados.com.br/)
[![Python](https://img.shields.io/badge/Python-3.12+-green?style=for-the-badge\&logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-blue?style=for-the-badge\&logo=pandas)](https://pandas.pydata.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Analytics-yellow?style=for-the-badge)](https://duckdb.org/)
[![Spark](https://img.shields.io/badge/Spark-Fast%20DataFrames-red?style=for-the-badge)](https://docs.databricks.com/aws/en/)
-----

## 📊 Fluxo do Projeto

![alt text](images\fluxo_projeto.png)

-----

## 📁 Estrutura do Projeto

```
02-python-big-data-processing/
├── src/
│   ├── create_measurements.py    # Gera arquivo de teste com 1 bilhão de linhas
│   ├── using_python.py            # Implementação em Python puro
│   ├── using_pandas.py           # Implementação com Pandas
│   ├── using_dask.py             # Implementação com Dask
│   ├── using_polars.py           # Implementação com Polars
│   ├── using_duckdb.py           # Implementação com DuckDB
│   └── using_bash_and_awk.sh      # Implementação em Bash + awk
├── data/
│   ├── measurements.txt          # Arquivo gerado com dados de teste
│   └── weather_stations.csv      # Lista de estações meteorológicas
├── pyproject.toml                # Dependências do projeto
└── README.md                     # Este arquivo
```

-----

## Técnicas Apresentadas

### ELT (Extract, Load, Transform)

**ELT** é a nova estratégia de tratamento de dados, o fluxo dela é :
***Extract***: Extração dos dados
***Load***: Duplicação das informações (banco de dados) da etapa de **Extração**
***Transform***: Tratamento dos dados

Uma das ferraments mais utilizadas para transformação de dados em SQL, hoje em dia é o ***dbt-core***,
onde você geralmente aplica essa estratégia de ***ELT*** nele, carregando o seu banco de dados e aplicando seu tratamento através do ***dbt***

-----

**Considerações**

Apesar do alto custo de **storage**, devido a duplicação do banco de dados, é um método eficiente já que em casos de problemas, erros e informações erradas, você falcilmente consegue indetificar essa questão sabendo se é um problema no dataset ou no framework(dbt).
Esse método era inviavel antigamente, devido ao alto custo de store, 1GB chegava a custar milhões de dolares

### ETL (Extract, Load, Transform)

**ETL** é uma estratégia de tratamento de dados já antiga e ainda utilizada, o fluxo dela é:
***Extract***: Extração dos dados
***Transform***: Transformação das informações, depois do carregamento dos dados na etapa **Extract**
***Load***: Disponibilização dos dados para consulmo

-----

**Considerações**

Esse modo de tratamento de dados é amplamente usado, pela eficiencia. Porém em questão a problema de visualização de dados era um pouco mais complicada, devido a não ser se os problemas proviam do dataset ou do framework utilizado para visualizar os dados, foi ai que veio a estratégia **ELT** mais pesada, porém mais fácil de governar. 

---
**Considerações**

O arquivo **weather_stations_sample.csv**, tem a lista de cidades em que os dados serão gerados pelo script **create_measurements.py**

---

### Load Less Data (Carregar Menos Dados)
Carregue menos dados, dados desnecessário, colunas, linhas e informações que não serão utilizadas

### Use Efficient Datatypes (Uso Eficiente de Tipo de Dados)

- Tipo ***category***:
    No SQL, quando temos uma coluna de cidade por exemplo, fazemos sempre uma nova tabela dimensão_cidade, oque é isso?
    Imagina que, na tabela principal os nomes das tabelas se repetem diversas vezes e toda vez que ela se repete, ela ocupa mais espaço na memória.
    Portanto, é extremamente útil criar uma dim_cidade, onde trocamos os valores em string da cidade, para nº int unitário. Assim, os valores das cidades que antes ocupavam mais memória,
    agora ocupam apenas um caracterer da memória.

    O tipo 'category' faz exatamente isso, ele categoriza os tipos de informações

**Exemplo de uso:**

df['name_column'] = df['name_column'].astype('category')

- Tipo ***float32***:
    O python, por padrão usa o float64 que armazena 15-17 dígitos portanto ocupa mais memória.
    É recomendado usar o float32, que armazena menos dígitos. Esse tipo é utilizando quando a velocidade é mais importante que a precisão

**Exempo de uso:**

df['name_column'] = df['name_column'].astype('float32')

### Chunksize
    Chunksize é uma estratégia onde, dividimos um dataset gigante em outros menores, para que a memória não seja estourada ela apenas aplicara as transformações, leitura e etc em um "pedaço" de 
    cada vez do dataset gigante.
    Existem prós e contras dessa estratégia, o contra é que demora mais para que o processa inteiro seja finalizado, porém o pró é que o seu processa rodará sem que você se preocupe com a memória da sua máquina.

**Observações**
DuckDB e Spark já possuem uma estrutura semelhante a ideia de 'chunksize' com os seus dados, sem você declarar isso no seu código. Portanto essa estratégia não precisa ser implementada em ambos, porém, ambos possuem estratégias diferentes:

- DuckDB: Trabalha com **Multiprocessamento**, ou seja, divide seu dataset em datasets menores, e cada dataset terá o seu core especifico rodando ele.

- Spark: Trabalha **Processamento Distribuído**, ou seja, divide seu dataset em datasets menores, e cada dataset terá o seu core e máquina rodando ele. Um **Processamento Distribuído** é quando há várias máquinas realizando **multiprocessamentos**

---

# Resultados

---

#### Python Puro
![alt text](images\py.png)

---

#### Pandas
![alt text](images\panda.png)

---

#### Duckdb
![alt text](images\duck.png)