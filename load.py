import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine 
import pandas as pd
import traceback

load_dotenv()
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")
HOST = "localhost"
PORT = "5433"

engine = create_engine(f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}",
                       client_encoding="utf8")

import traceback

def load_to_postgres(df: pd.DataFrame, table_name: str = 'tb_livros_cinema'):
    try:
        df.to_sql(name=table_name,
                  con=engine,
                  if_exists="replace",
                  index=False)
        print(f"Tabela '{table_name}' criada com {len(df)} registros.")
        return True

    except Exception as e:
        print(f'Erro ao carregar dados no PostgreSQL: {e}')
        return False

if __name__ == "__main__":
    print("Load pronto para ser chamado pelo main")

