# Requisitos do projeto:
# Requisito a: "O projeto deve suportar duas culturas"
# Na function chamada "modulo 1"  declaramos que apenas milho ou soja serão aceitos

# Requisito b: "Cálculo da área de plantio para cada cultura"
# Na function "modulo 1" fazemos uma chamada para a function "calcular_area_insumo" que efetua este cálculo.

# Requisito c: "Cálculo do manejo de insumos"
# Aqui também aproveitamos a function "calcular_area_insumo" e efetuamos este cálculo.

# Requisito d: "Os dados devem estar organizados em vetores"
# Utilizamos três vetores no programa: "vetorcultura", "vetorinsumo" e "vetorarea" para armazenamento de dados.

# Requisito e: "A aplicação Python precisa ter um menu de opções"
# O módulo "exibir_menu" contempla esta necessidade.

# Requisito f: "Usar rotinas de loop e decisão"
# Estas rotinas foram usadas tanto no módulo "exibir_menu" quanto no módulo "modulo 1", por exemplo.

# Requisito g: "Usar esses dados para desenvolver uma aplicação em R..."
# Como os dados são armazenados em vetores, eles são perdidos ao término do programa.
# Utilzei o módulo "csv" para salvar os dados em um arquivo e desta forma utiliza-lo mais adiante.
# O formato deste arquivo contém o header e os registros, como demostrado abaixo, como exemplo:
# -------------------
# Cultura,Area,Insumo
# soja,529.0,15.87
# soja,1156.0,34.68
# -------------------

import csv
import os

# Dados
vetorcultura = []
vetorinseticida = []
vetorarea = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir mensagens com formatação
def exibir_mensagem(mensagem):
    yellow = "\033[93m"
    reset = "\033[0m"
    print("\n" + yellow + mensagem + reset + "\n" + "-" * len(mensagem))

clear_screen()
exibir_mensagem("Bem-vindo ao aplicativo FarmTech! Esse aplicativo vai trabalhar com duas culturas: Milho e Soja.")

def salvar_dados_csv():
    file_exists = os.path.isfile('dados_farmtech.csv')

    # Verifica a existência do cabeçalho se o arquivo existir
    header_exists = False
    if file_exists:
        with open('dados_farmtech.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            first_row = next(reader, None)
            header_exists = first_row is not None and first_row[0] == 'Cultura'

    # Abre o arquivo em modo de append
    with open('dados_farmtech.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not header_exists:
            writer.writerow(['Cultura', 'Área', 'inseticida'])
        
        for i in range(len(vetorcultura)):
            writer.writerow([vetorcultura[i], vetorarea[i], vetorinseticida[i]])
    
    exibir_mensagem("Os dados foram salvos no arquivo 'dados_farmtech.csv'.")

def calcular_area_inseticida(tipo_cultura, largura, comprimento):
    area = largura * comprimento
    inseticida_por_metro = area * 0.05 if tipo_cultura == 'milho' else area * 0.03
    return area, inseticida_por_metro

def input_float(prompt):
    while True:
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("O número deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def modulo1():
    exibir_mensagem("Inserção de Dados")
    while True:
        tipo_cultura = input("Digite o tipo de cultura (milho/soja): ").lower()
        if tipo_cultura in ['milho', 'soja']:
            largura = input_float(f"Digite a largura do terreno da plantacao de {tipo_cultura} (em metros): ")
            comprimento = input_float(f"Digite o comprimento do terreno da plantacao de {tipo_cultura} (em metros): ")
            area, inseticida_por_metro = calcular_area_inseticida(tipo_cultura, largura, comprimento)
            area = round(area, 2)
            inseticida_por_metro = round(inseticida_por_metro, 2)
            exibir_mensagem(f"Para {tipo_cultura}, as seguintes informações foram adicionadas:\n"
                            f"Área total do terreno: {area:.2f} metros quadrados\n"
                            f"inseticida necessário: {inseticida_por_metro:.2f} litros de inseticida")
            vetorcultura.append(tipo_cultura)
            vetorinseticida.append(inseticida_por_metro)
            vetorarea.append(area)
            print("Dados inseridos com sucesso!\n")
            break
        else:
            print("Cultura desconhecida. Tente novamente.")

def modulo2():
    exibir_mensagem("Exibição de Dados")
    if not vetorarea:
        exibir_mensagem("A base de dados ainda está vazia, por favor tente mais tarde!")
    else:
        for i, cultura in enumerate(vetorcultura):
            print(f"{i+1} - Área plantada de {cultura} com {vetorarea[i]:.2f} m², "
                  f"que necessitam de {vetorinseticida[i]:.2f} litros de inseticidas.")

def modulo3():
    exibir_mensagem("Atualização de Dados")
    if not vetorarea:
        exibir_mensagem("A base de dados ainda está vazia, por favor tente mais tarde!")
        return

    print("Registros atuais:")
    for i, cultura in enumerate(vetorcultura):
        print(f"{i+1} - {cultura.capitalize()}, Área: {vetorarea[i]:.2f} m², inseticida: {vetorinseticida[i]:.2f} litros")

    while True:
        try:
            escolha = int(input(f"\nEscolha o número do registro que deseja alterar (1-{len(vetorcultura)}): "))
            if 1 <= escolha <= len(vetorcultura):
                escolha -= 1
                break
            else:
                print("Número inválido. Escolha um registro válido.")
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"\nVocê selecionou o registro {escolha+1}: {vetorcultura[escolha].capitalize()}, "
          f"Área: {vetorarea[escolha]:.2f} m², inseticida: {vetorinseticida[escolha]:.2f} litros")

    print("\nAtualizando os valores...")
    nova_largura = input_float(f"Digite a nova largura do terreno da plantação de {vetorcultura[escolha]} (em metros): ")
    novo_comprimento = input_float(f"Digite o novo comprimento do terreno da plantação de {vetorcultura[escolha]} (em metros): ")
    nova_area, novo_inseticida = calcular_area_inseticida(vetorcultura[escolha], nova_largura, novo_comprimento)

    vetorarea[escolha] = round(nova_area, 2)
    vetorinseticida[escolha] = round(novo_inseticida, 2)

    exibir_mensagem(f"Registro {escolha+1} atualizado com sucesso!\n"
                    f"Nova área: {vetorarea[escolha]:.2f} m², Novo inseticida: {vetorinseticida[escolha]:.2f} litros")

def modulo4():
    exibir_mensagem("Exclusão de Dados")
    if not vetorarea:
        exibir_mensagem("A base de dados ainda está vazia, por favor tente mais tarde!")
        return

    print("Registros atuais:")
    for i, cultura in enumerate(vetorcultura):
        print(f"{i+1} - {cultura.capitalize()}, Área: {vetorarea[i]:.2f} m², inseticida: {vetorinseticida[i]:.2f} litros")

    while True:
        try:
            escolha = int(input(f"\nEscolha o número do registro que deseja excluir (1-{len(vetorcultura)}): "))
            if 1 <= escolha <= len(vetorcultura):
                escolha -= 1
                break
            else:
                print("Número inválido. Escolha um registro válido.")
        except ValueError:
            print("Por favor, insira um número válido.")

    confirmacao = input(f"Tem certeza que deseja excluir o registro {escolha+1}: {vetorcultura[escolha].capitalize()}, "
                        f"Área: {vetorarea[escolha]:.2f} m², inseticida: {vetorinseticida[escolha]:.2f} litros? (s/n): ").lower()

    if confirmacao == 's':
        del vetorcultura[escolha]
        del vetorarea[escolha]
        del vetorinseticida[escolha]
        exibir_mensagem(f"Registro {escolha+1} excluído com sucesso!")
    else:
        print("\nA exclusão foi cancelada.")

def exibir_menu():
    while True:
        print("\nMenu Principal:")
        print("1 - Inserção de Dados")
        print("2 - Exibição de Dados")
        print("3 - Atualização de Dados")
        print("4 - Exclusão de Dados")
        print("5 - Sair do Programa")
        print("")

        escolha = input("Escolha uma opção: ")

        if escolha == '5':
            confirmacao = input("Tem certeza que deseja sair? (s/n): ").lower()
            if confirmacao == 's':
                salvar_dados_csv()
                exibir_mensagem("Saindo...")
                break
        elif escolha in modulos:
            modulos[escolha]()
        else:
            print("Opção inválida. Tente novamente.")

# Menu de opções
modulos = {
    '1': modulo1,
    '2': modulo2,
    '3': modulo3,
    '4': modulo4,
}
# Chama o menu
exibir_menu()