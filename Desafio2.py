n = int(0)
a1 = int(-2)
a2 = int(-1)
a3 = int(0)
a4 = int(1)
a5 = int(2)

if a1 >= 0:
    n = n + 1
if a2 >= 0:
    n = n + 1
if a3 >= 0:
    n = n + 1
if a4 >= 0:
    n = n + 1
if a5 >= 0:
    n = n + 1

if n >= 3:
    print("Aula Normal")
    print("O numero de alunos presente é : ",n)
else:
    print("Aula Cancelada")
    print("O numero de alunos presente é : ",n)