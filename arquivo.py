import ntpath
import pyodbc

# Configuração da conexão com o banco de dados
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=VARJAO_2021;'
    'UID=sa;'
    'PWD=Jack@frost!'
)

# cursor = conn.cursor()
# cursor.execute("SELECT 1")
# print("Conexão bem-sucedida!")
# exit()

# Consulta para obter todos os BLOBs
query = "SELECT Nome_Anexo as nome_arquivo, Anexo as conteudo FROM Contrato"

with conn.cursor() as cursor:
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        contador = 1
        for nome_arquivo, conteudo in rows:
            if not conteudo:
                print(f"Arquivo ignorado: {nome_arquivo or 'Sem nome'} (conteúdo vazio ou corrompido)")
                continue
            
            # Extrair apenas o nome do arquivo
            nome_arquivo = ntpath.basename(nome_arquivo) if nome_arquivo else f"file_{contador}.pdf"
            contador += 1
            
            with open(nome_arquivo, 'wb') as file:
                file.write(conteudo)
            print(f"Arquivo {nome_arquivo} salvo com sucesso!")
    else:
        print("Nenhum registro encontrado.")