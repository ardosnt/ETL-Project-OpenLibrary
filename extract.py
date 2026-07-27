import requests

def request_openlibrary(endpoint1: str, endpoint2: str, limit: int = 100):
    response = requests.get(f"https://openlibrary.org/{endpoint1}/{endpoint2}.json?limit={limit}")
    if response.status_code == 200:
        print("Dados extraídos com sucesso!")
        return response.json()
    else:
        print("Erro na requisição")


if __name__ == "__main__":
    data = request_openlibrary("subjects", "cinema")