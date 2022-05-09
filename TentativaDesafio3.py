v1 = int(input("Digite o primeiro vetor : "))
v2 = int(input("Digite o segundo vetor : "))
v3 = int(input("digite o terceiro vetor : "))

N = 10

a1 = v1 * v1
a2 = v1 * v2
a3 = v1 * v3

b1 = v2 * v1
b2 = v2 * v2
b3 = v2 * v3

c1 = v3 * v1
c2 = v3 * v2
c3 = v3 * v3

if a1 <= N:
    print(f"verdadeiro {a1} a1")
if a2 <= N:
    print(f"verdadeiro {a2} a2")
if a3 <= N:
    print(f"verdadeiro {3} a3")
    
if b1 <= N:
    print(f"verdadeiro {b1} b1")
if b2 <= N:
    print(f"verdadeiro {b2} b2")
if b3 <= N:
    print(f"verdadeiro {b3} b3")
    
if c1 <= N:
    print(f"verdadeiro {c1} c1")
if c2 <= N:
    print(f"verdadeiro {c2} c2")
if c2 <= N:
    print(f"verdadeiro {c3} c3")
    
    