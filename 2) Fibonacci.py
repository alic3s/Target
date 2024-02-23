def fibonacci(numero):
    a = 0
    b = 1
    cont = 3
    fibo = [a, b]
    while cont <= numero:
        c = a + b
        fibo.append(c)
        a = b
        b = c
        cont += 1
    return numero in fibo, fibo

num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print()
pertence, fibo = fibonacci(num)

if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
print()
print("Sequência de Fibonacci até o número {}: {}".format(num, fibo))
