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
C5 --> D

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