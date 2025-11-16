"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

# Converte para Celsius primeiro
if origem == "C":
    celsius = temp
elif origem == "F":
    celsius = (temp - 32) * 5/9
elif origem == "K":
    celsius = temp - 273.15
else:
    print("Unidade inválida!")
    exit()

# Converte para destino
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9/5) + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidade inválida!")
    exit()

print(f"{temp}°{origem} = {resultado:.2f}°{destino}")