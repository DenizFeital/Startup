# Carregar a biblioteca necessária
library(dplyr)

# Carregar o arquivo CSV
dados <- read.csv("dados_farmtech.csv")

# Exibir os primeiros registros para verificar os dados
head(dados)

# Calcular a média e o desvio padrão por Cultura
estatisticas <- dados %>%
  group_by(Cultura) %>%
  summarise(
    Media_Area = mean(Area, na.rm = TRUE),
    Desvio_Padrao_Area = sd(Area, na.rm = TRUE),
    Media_Insumo = mean(Insumo, na.rm = TRUE),
    Desvio_Padrao_Insumo = sd(Insumo, na.rm = TRUE)
  )

# Exibir as estatísticas calculadas
print(estatisticas)
