n = 100
ninvertido = 0
a5 = 0
while n <= 100000:
    n = n + 1
    centenamilhar = (n%1000000)//100000
    dezenamilhar = (n%100000)//10000
    unidademilhar = (n%10000)//1000
    centena = (n%1000)//100  #n//100
    dez = (n%100)//10
    unidade = n%10
    a1 = (unidade*100000)+(dez*10000)+(centena*1000)+(unidademilhar*100)+(dezenamilhar*10)+(centenamilhar*1)
    soma = a1 + n
    resultado = soma % 2
    if resultado == 1:
        a5 = a5 + 1
        print(f"O valor invertido e a soma é : {n} + {unidade}{dez}{centena}{unidademilhar}{dezenamilhar}{centenamilhar} = {n + a1} e deu {a5} resultados")   
