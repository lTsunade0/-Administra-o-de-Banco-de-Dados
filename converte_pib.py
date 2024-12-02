import csv

# Caminho relativo para o arquivo original e o arquivo corrigido
arquivo_original = "pib.csv"  # Arquivo está na mesma pasta do script
arquivo_corrigido = "pib_corrigido.csv"  # Novo arquivo gerado na mesma pasta

# Abrir o arquivo original e processar
with open(arquivo_original, "r", encoding="utf-8") as entrada, open(arquivo_corrigido, "w", newline='', encoding="utf-8") as saida:
    leitor = csv.reader(entrada, delimiter=';')  # O original usa ponto e vírgula como delimitador
    escritor = csv.writer(saida, delimiter=',')  # Novo formato com vírgula como delimitador

    for linha in leitor:
        # Ignorar linhas vazias
        if not any(linha):
            continue

        # Extraindo os campos
        data = linha[0]
        estado = linha[1]
        nome_cidade = linha[2]
        pib = linha[5].strip().replace('.', '').replace(',', '.')  # Ajusta o formato do PIB

        # Ignorar entradas com campos obrigatórios vazios
        if data and estado and nome_cidade and pib:
            escritor.writerow([data, estado, nome_cidade, pib])

print("Arquivo corrigido salvo em:", arquivo_corrigido)
