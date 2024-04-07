#Excersise 5.1

import os

def find_pdf_size(top):
    size_pdf = 0  
    for root, dirs, files in os.walk(top):
       for name in files:
            if name.lower().endswith(".pdf"):   
                 file_path = os.path.join(root, name)
                 size_pdf += os.path.getsize(file_path)
    return size_pdf

print("The size of pdf files is:", find_pdf_size("."), "bytes")



#Excersise 5.2

from datetime import datetime


def print_working_days(date1, date2):
    start_date = datetime.strptime(date1, '%Y-%m-%d')
    end_date = datetime.strptime(date2, '%Y-%m-%d')
    
    while start_date < end_date:
        if start_date.weekday() < 5:
            print(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
            
print_working_days('2024-04-01', '2024-05-01')            


#Excersise 5.3

import random

def random_walk(start):
    new_position = start
    for i in range(100):
        move = random.choice([-1, 1])
        new_position += move
        yield new_position
        
random_walker = random_walk(0)
final_position = None
for new_position in random_walker:
    final_position = new_position
print("Position after 100 moves:", final_position)
