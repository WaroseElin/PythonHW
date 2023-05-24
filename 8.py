n = int(input("Введите длину шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите кол-во долек, которое Вы хотите взять: "))
if k < n*m and (k % n == 0 or k % m == 0):
   if n * m >= k and (k % m == 0 or k % n == 0):
    print("yes")
else:
    print("no")
