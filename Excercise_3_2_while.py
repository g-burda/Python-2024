#3.2 while
print ("Exercise 3.2 WHILE")
i=0
while i < 40:
    i = i + 1
    if i % 5 == 0:
        print(f'{i} is divided by 5' )
    if i % 7 == 0:
        print(f'{i} is divided by 7' )
    if i % 5 == 0 and i % 7 == 0:
        print(f'{i} is divided by 5 and 7' )
    if i==13:
        continue
    if i % 5 != 0 and i % 7 != 0:
        print(f'{i} is not important' )
