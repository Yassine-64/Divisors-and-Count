nombre = int(input("entrez un entier :"))
n_diviseur = 0
for i in range(1, nombre+1):
    if nombre % i == 0:
        print(i)
        n_diviseur = n_diviseur + 1
print("le nombre total des diviseurs est :", n_diviseur)