from extract import request_openlibrary
import pandas as pd


def transform_data(data_json: dict):
    df_raw = pd.DataFrame(data_json.get("works", []))

    #Filtrando colunas
    cols = ['key', 'title', 'first_publish_year', 'edition_count', 'authors']
    df = df_raw[cols]

    #Filtrando nome real do autor e dropando tabela antiga
    df['author_name'] = df['authors'].apply(lambda x: x[0]['name'] if isinstance(x, list) and len(x) > 0 else None)
    df = df.drop(columns=["authors"])

    #Limpando a key
    df['key'] = df['key'].str.replace('/works/', '', regex=False)

    return df


    



    


    