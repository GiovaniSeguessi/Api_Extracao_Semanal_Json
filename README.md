# Coletor de Dados da API

## Descrição do Projeto

Este projeto consiste em uma aplicação Python para coletar dados de uma API específica em intervalos diários ao longo de uma semana. Ele utiliza a biblioteca `requests` para fazer solicitações HTTP à API e a biblioteca `json` para manipulação dos dados em formato JSON. 

### Propósito

O propósito desta aplicação é coletar dados relevantes para análise de um cliente específico. O código realiza as seguintes etapas:
1. Define as datas de início e fim da coleta com base na data atual, capturada através do módulo `datetime`.
2. Autentica-se na API usando um token de autenticação, que é utilizado para realizar as consultas posteriores.
3. Realiza uma consulta inicial para obter o número total de páginas de dados disponíveis para cada dia no intervalo definido.
4. Percorre todas as páginas de dados para cada dia, coletando as informações e armazenando-as em uma lista chamada `all_data`.
5. Ao final da coleta, os dados são salvos em um arquivo JSON chamado "data.json" no diretório do script.