from extract import request_openlibrary
from transform import transform_data
from load import load_to_postgres

def run():
    raw_json = request_openlibrary("subjects", "cinema", limit=100)
    df_clean = transform_data(raw_json)
    load_to_postgres(df_clean, 'tb_livros_cinema')
    print("\n PIPELINE FINALIZADO COM SUCESSO!")

if __name__ == "__main__":
    run()



