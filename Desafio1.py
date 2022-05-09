n = 1000
ninvertido = 0
while n <= 9000:
    n = n + 1
    unidademilhar = (n%10000)//1000
    centena = (n%1000)//100  #n//100
    dez = (n%100)//10
    unidade = n%10
    a1 = (unidade*1000)+(dez*100)+(centena*10)+(unidademilhar*1)
    resultado = (n + a1)%2
    if resultado == 1:
            print(f"O valor invertido e a soma é : {n} + {unidade}{dez}{centena}{unidademilhar} = {n + a1}")   
