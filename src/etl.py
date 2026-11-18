import pandas as pd
import numpy as np
import os

def extrair_dados(caminho_raw: str) -> pd.DataFrame:
    print(f"Lendo arquivo bruto de: {caminho_raw}")
    df_raw = pd.read_excel(caminho_raw, sheet_name='T 728')
    return df_raw

def transformar_dados(df_raw: pd.DataFrame) -> pd.DataFrame:
    data_rows = []
    for idx in range(7, 38):
        row = df_raw.iloc[idx]
        data_rows.append({
            'ano': int(row.iloc[0]),
            'onibus': float(row.iloc[1]) if pd.notna(row.iloc[1]) and row.iloc[1] != '...' else np.nan,
            'metro': float(row.iloc[2]) if pd.notna(row.iloc[2]) and row.iloc[2] != '...' else np.nan,
            'trem': float(row.iloc[3]) if pd.notna(row.iloc[3]) and row.iloc[3] != '...' else np.nan,
            'bonde': float(row.iloc[4]) if pd.notna(row.iloc[4]) and row.iloc[4] != '...' else np.nan,
            'hidroviario': float(row.iloc[5]) if pd.notna(row.iloc[5]) and row.iloc[5] != '...' else np.nan,
            'aeroviario': float(row.iloc[6]) if pd.notna(row.iloc[6]) and row.iloc[6] != '...' else np.nan,
        })
    
    df = pd.DataFrame(data_rows)
    df.loc[(df['ano'] >= 2012) & (df['ano'] <= 2014), 'bonde'] = 0.0
    df['total_passageiros'] = df[['onibus', 'metro', 'trem', 'bonde', 'hidroviario', 'aeroviario']].sum(axis=1)
    
    return df

def carregar_dados(df: pd.DataFrame, caminho_destino: str):
    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
    df.to_csv(caminho_destino, compression='gzip', index=False)
    print(f"Dados processados salvos com sucesso em: {caminho_destino}")

if __name__ == "__main__":
    raw_path = "data/raw/728.xls"
    processed_path = "data/processed/passageiros_rio_tratado.csv.gz"
    
    raw_df = extrair_dados(raw_path)
    clean_df = transformar_dados(raw_df)
    carregar_dados(clean_df, processed_path)
    print("Pipeline ETL executado com sucesso!")