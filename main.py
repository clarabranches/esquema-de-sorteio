import random

valores = ["doce","salgado","os dois"]
probabilidade = [0.34, 0.33, 0.33]

r = [1,2,3]
reoganizar = random.choice(r)
if reoganizar == 1:
    probabilidade = [0.34, 0.33, 0.33]
elif reoganizar == 2:
    probabilidade = [0.33, 0.34, 0.33]
else:
    probabilidade = [0.33, 0.33, 0.34]

print(probabilidade)
resultado = random.choices(valores, probabilidade)
print(resultado[0])