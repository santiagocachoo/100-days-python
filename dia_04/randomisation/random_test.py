import random
import my_module as mm

random_int = random.randint(1, 10)

print(random_int)
print(mm.numero_favorito)


numero_super_random = random.random() * 10
print(numero_super_random)

numero_aun_mas_random = random.uniform(1, 10)
print(numero_aun_mas_random)