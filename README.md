# Criacao de um programa em Python para tratar duas culturas de uma empresa de agricultura.
# O sistema deve incluir opcoes para incluir, mostrar, alterar e apagar recursos.
# Alem disso, os requisitos abaixo devem ser atendidos.

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
