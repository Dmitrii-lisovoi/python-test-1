#Ціна на товар
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffe_pack = 4.42
#Кількістькожного продукту
num_croissant = int(input("Введіть кількість круасанів:"))
num_glasses = int(input("Введіть кількість стаканчиків:"))
num_coffe_pack = int(input("Введіть кількість упаковок кави:"))
#Обчислення загальної вартості
total_cost = num_croissant * price_per_croissant + num_glasses * price_per_glass + num_coffe_pack * price_per_coffe_pack
#кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)
#Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars}")
print(f"Загальна Вартість у центах: {total_cents}")
