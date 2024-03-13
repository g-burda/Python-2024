#3.2 for
print ("Exercise 3.2 FOR")
for y in range(1, 41):
    if y % 5 == 0:
        print(f'{y} is divided by 5' )
    if y % 7 == 0:
        print(f'{y} is divided by 7' )
    if y % 5 == 0 and y % 7 == 0:
        print(f'{y} is divided by 5 and 7' )
    if y==13:
        continue
    if y % 5 != 0 and y % 7 != 0:
        print(f'{y} is not important' )