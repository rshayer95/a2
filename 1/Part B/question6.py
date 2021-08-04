input = str(input("Enter any text string: "))

for i in range(31):
    if i == 21:
        continue
    print(i ," ", input , "\n")
    if i == 26:
        break