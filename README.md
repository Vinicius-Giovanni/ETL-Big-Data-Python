# Projeto: ETL Big Data Python
-----

## 📋 Sobre

Este projeto demonstra como processar eficientemente **1 bilhão de linhas de dados** (~14GB) usando diferentes abordagens em Python. O desafio é calcular estatísticas (mínimo, média e máximo) de temperaturas por estação meteorológica, comparando o desempenho de várias bibliotecas e técnicas.

[![Projeto](https://img.shields.io/badge/Projeto-Big%20Data-blue?style=for-the-badge)](https://suajornadadedados.com.br/)
[![Python](https://img.shields.io/badge/Python-3.12+-green?style=for-the-badge\&logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-blue?style=for-the-badge\&logo=pandas)](https://pandas.pydata.org/)
[![Dask](https://img.shields.io/badge/Dask-Distributed-orange?style=for-the-badge)](https://dask.org/)
[![Polars](https://img.shields.io/badge/Polars-Fast%20DataFrames-red?style=for-the-badge)](https://pola-rs.github.io/polars/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Analytics-yellow?style=for-the-badge)](https://duckdb.org/)

-----

## 📊 Fluxo do Projeto

```mermaid
graph TD
A[Arquivo CSV<br/>1 Bilhão de linhas<br/>~14GB] --> B{Abordagem}

B --> |Python Puro| C1[20 min]
B --> |Pandas| C2[263 seg]
B --> |Duckdb| C3[155 seg]
B --> |PySpark| C4[14 seg]

C1 --> D[Estatísticas por Estação<br/>Min, Média, Max]
C2 --> D
C3 --> D
C4 --> D

style A fill:#e1f5ff
style C5 fill:#c8e6c9
style D fill:#fff3e0
```

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

#### Considerações
Apesar do alto custo de **storage**, devido a duplicação do banco de dados, é um método eficiente já que em casos de problemas, erros e informações erradas, você falcilmente consegue indetificar essa questão sabendo se é um problema no dataset ou no framework(dbt).
Esse método era inviavel antigamente, devido ao alto custo de store, 1GB chegava a custar milhões de dolares

### ETL (Extract, Load, Transform)

**ETL** é uma estratégia de tratamento de dados já antiga e ainda utilizada, o fluxo dela é:
***Extract***: Extração dos dados
***Transform***: Transformação das informações, depois do carregamento dos dados na etapa **Extract**
***Load***: Disponibilização dos dados para consulmo

-----

#### Considerações
Esse modo de tratamento de dados é amplamente usado, pela eficiencia. Porém em questão a problema de visualização de dados era um pouco mais complicada, devido a não ser se os problemas proviam do dataset ou do framework utilizado para visualizar os dados, foi ai que veio a estratégia **ELT** mais pesada, porém mais fácil de governar. 

---
## Considerações

O arquivo **weather_stations_sample.csv**, tem a lista de cidades em que os dados serão gerados pelo script **create_measurements.py**