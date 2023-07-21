# Código para Coleta de Dados de uma API e Salvamento em JSON

import requests
import json
import datetime

# seta o cabeçalho
headers = {
    "Content-Type": "application/json"
}

# Obter a data atual
current_date = datetime.datetime.now()

# Definir as datas de início e fim
start_date = current_date - datetime.timedelta(days=7)
end_date = current_date - datetime.timedelta(days=1)

# Converter as datas para objetos do tipo datetime
start_date_str = start_date.strftime("%d/%m/%Y")
end_date_str = end_date.strftime("%d/%m/%Y")

# Lista para armazenar todos os dados coletados
all_data = []

# Loop para percorrer as datas do intervalo e coletar os dados
current_date = start_date
while current_date <= end_date:
    current_date_str = current_date.strftime("%d/%m/%Y")

    # Define a carga do request como dicionário
    payload = {
        "password": "XXXX",
        "cliente": "xxxxx"
    }

    # Envia uma solicitação HTTP POST para o endpoint de autentificação
    response = requests.post("https://XXXX", headers=headers, data=json.dumps(payload))

    # Verifica se a resposta obteve sucesso
    if response.status_code == 200:
        json_data = response.json()
        token = json_data["token"]
    else:
        print("Requisição do token falhou")
        exit()
    
    # Define os filtros para a consulta
    payload = {
        "identifier": "XX",
        "filters": {
            "page": 1,
            "size": 10000,
            "data": current_date_str
        }
    }

    # Define os cabeçalhos com o token de autenticação
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }

    # Envia uma solicitação HTTP POST para obter os dados da API
    response = requests.post("https://XXXX", headers=headers, data=json.dumps(payload))

    # Verifica se a resposta obteve sucesso
    if response.status_code == 200:
        json_data = response.json()
        total_pages = json_data["total_pages"]
        print(f"Número de páginas: {total_pages}")
    else:
        print("Requisição da carga falhou", response.status_code)
        exit()

    # Loop para percorrer todas as páginas e coletar os dados
    for page in range(1, total_pages + 1):
        payload["filters"]["page"] = page
        response = requests.post("https://XXXX", headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            json_data = response.json()
            data = json_data["data"]
            all_data.extend(data)
            print(f"Dados retirados com sucesso da página {page} do dia {current_date_str}")
        else:
            print(f"Dados não foram retirados da página {page} do dia {current_date_str}")

    # Avança para o próximo dia
    current_date += datetime.timedelta(days=1)

# Salva os dados coletados em um arquivo JSON
json_file_path = "data.json"
with open(json_file_path, "w") as file:
    json.dump(all_data, file)

print("Dados salvos com sucesso")
