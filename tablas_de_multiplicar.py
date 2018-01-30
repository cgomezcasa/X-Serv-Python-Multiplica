#!usr/bin/python

num = list(range(1,11))
for n in num:
    print("Tabla de multiplicar del ", n)
    for m in num:    
        result = n*m
        print(n," por ",m," es ",result)

