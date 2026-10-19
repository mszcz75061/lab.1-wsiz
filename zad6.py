import random
droga = random.randint(1,1000)
spalanie = float(input("Podaj spalanie na 100km: "))
cena_paliwa = 6.5

koszt = (droga / 100) * spalanie * cena_paliwa
print(f"Koszt przejazdu, {droga}km, przy spalaniu {spalanie} l/100km i cenie paliwa {cena_paliwa} zł/l wynosi: {koszt:.2f} zł")