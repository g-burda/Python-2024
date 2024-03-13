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