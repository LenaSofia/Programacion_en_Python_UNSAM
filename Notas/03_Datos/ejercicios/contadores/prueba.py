from collections import Counter

camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

verduleria = Counter()

for nombre, cantidad, precio in camion:
    verduleria[nombre] += cantidad * precio

print(verduleria["camisas"])
