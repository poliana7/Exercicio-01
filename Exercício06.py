altura = float(input("digite a sua altura em metro (ex: 1,70):"))
peso = float(input("digite o seu peso em kg (ex: 65):"))
imc = peso / (altura ** 2)
print(f"seu imc é: {imc:.2f}")