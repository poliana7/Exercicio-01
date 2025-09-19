# Função que converte dias, horas, minutos e segundos para total de segundos
def converter_para_segundos(dias, horas, minutos, segundos):
    # Calculando o total de segundos
    total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Leitura dos valores
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Calculando o total de segundos
total_segundos = converter_para_segundos(dias, horas, minutos, segundos)

# Exibindo o resultado
print(f"O total de segundos é: {total_segundos}")
