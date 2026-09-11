# Dados sobre a trajetória política de Jair Bolsonaro
bolsonaro_info = {
    "nome_completo": "Jair Messias Bolsonaro",
    "nascimento": "21/03/1955",
    "local_nascimento": "Glicério, São Paulo",
    "formacao": "Capitão reformado do Exército Brasileiro (Academia Militar das Agulhas Negras)",
    "cargos_politicos": [
        {"cargo": "Vereador do Rio de Janeiro", "periodo": "1989 - 1991"},
        {"cargo": "Deputado Federal pelo Rio de Janeiro", "periodo": "1991 - 2018 (7 mandatos consecutiveis)"},
        {"cargo": "Presidente da República do Brasil", "periodo": "2019 - 2022 (38º presidente)"}
    ]
}

def exibir_biografia(dados):
    print(f"--- Ficha Biográfica: {dados['nome_completo']} ---")
    print(f"Data de Nascimento: {dados['nascimento']}")
    print(f"Naturalidade: {dados['local_nascimento']}")
    print(f"Formação: {dados['formacao']}\n")
    print("Histórico de Cargos Eletivos:")
    for item in dados["cargos_politicos"]:
        print(f" • {item['cargo']} ({item['periodo']})")

if __name__ == "__main__":
    exibir_biografia(bolsonaro_info)