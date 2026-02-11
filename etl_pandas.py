# Processo de Pandas para 100 milhões de linhas foi em 64.51 sec
import pandas as pd
from multiprocessing import Pool, cpu_count # cpu_count conta a qt de cpus disponiveis
from tqdm import tqdm # importa a barra de progresso

CONCURRENCY = cpu_count()

total_linhas = 100000000 # Total de linhas conhecido
chunksize = 100000 # Define o tamanho da chunk
filename = "data/measurements.txt"

def process_chunk(chunk):
    # Agrega os dados dentro do chunk usando Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min','max','mean']).reset_index() # Agrupando, usando soma das colunas criadas
    return aggregated

def create_df_with_pandas(filename, total_linhas, chunksize=chunksize):
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0) # div. int qt de pedacos de chunk, se sobrar algo no cal de moda, ele somará +1 chunk na cont
    results = []

    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader: # Quando usamos chunk, o read_csv n retorna um df, ele retorna um TextFileReader, q é um iterador
        # Envolvendo o iterador com tqdm para visualizar o progresso
        with Pool(CONCURRENCY) as pool:
            """
            Criando um pool de processo
            - CONCURRENCY = nºde processos paralelos, cada processo roda process_chunk.
            - Isso usa múltiplos cores da CPU
            """
            for chunk in tqdm(reader, total=total_chunks, desc= "           Processando"):
                # Processa cada chunk em paralelo
                result = pool.apply_async(process_chunk, (chunk,)) # Guard. obj. AsycResult. N estamos guard. dfs ainda. Estamos guard. obj. AsyncResult
                results.append(result)
            
            results = [result.get() for result in results]
        
    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min':'min',
        'max':'max',
        'mean':'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Iniciando o processamento de arquivo.")
    start_time = time.time()
    df = create_df_with_pandas(filename, total_linhas, chunksize)
    took = time.time() - start_time

    print(df.head())
    print(f"Processing took: {took:.2f} sec")
