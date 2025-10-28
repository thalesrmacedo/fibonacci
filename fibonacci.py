n = int(input("Qual termo de Fibonacci você quer? "))
ultimo=1
penultimo=0

if n==0:
    print("Não existe")
elif n==1:
    print("1")
else:
    for contador in range(1,n):
        termo = ultimo + penultimo 
        penultimo = ultimo
        ultimo = termo
        contador +=1
    print("O termo",n,"de Fibonacci é",termo)
    