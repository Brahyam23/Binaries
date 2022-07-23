#Definir una función max() que tome como argumento
#dos númerosy devuelva el mayor de ellos.

def bin(num):
    binario = ""

    while not num == 1:
        binario += str(num%2)
        num //= 2
    binario += str(num%2)
    binario= binario[::-1]

    return binario

def dec(num):
    c = 0
    num = str(num)
    num = num[::-1]
    resultado = 0

    for i in num:
        resultado += int(i) * (2 ** c)
        c += 1

    return resultado

print(bin(172))
print(dec(10101100))


