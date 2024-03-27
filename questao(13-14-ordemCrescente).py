'''
Enunciado: Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
fatorial.
'''
def fatorial(num):
    if num<0:
        return "Valor inválido, o valor fornecido é negativo"
    elif num == 0:
        return 1
    else:
        resultado = 1

        etapas = "1"

        for i in range(2, num + 1):
            resultado*= i
            etapas += f".{i}"
        return f"Fatorial de {num} = {etapas} = {resultado}"
            
num = int(input("Informe um número natural: "))

print(fatorial(num))
