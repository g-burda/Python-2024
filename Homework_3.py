#3.1
print ("Exercise 3.1")
def print_word_in_squares(word):
    word_len = len(word)
    top_bottom_line = "+---" * word_len + "+"
    word_line = "| {} " * word_len + "|"

    print(top_bottom_line)
    print(word_line.format(*word))
    print(top_bottom_line)

name = input("Please enter your name: ")
print_word_in_squares(name)


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


#3.3
print ("Exercise 3.3")
import math

n = 2022
x = f'{math.pi:.5f}'
word = "Python"
polish = "książka"

with open('vars.txt', 'w') as outfile:
    outfile.write(str(n))
    outfile.write("\n")
    outfile.write(x)
    outfile.write("\n")
    outfile.write(word)
    outfile.write("\n")
    outfile.write(polish)

outfile.close()

with open('vars.txt', 'r') as infile: 
    text = infile.read()

print(text)