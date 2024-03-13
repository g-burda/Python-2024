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