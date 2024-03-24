#Exercise 4.1

point_list = [(0,0), (-1,1), (3,4), (9,10), (-6,10), (-100, -2), (1,2)]

points_in_unit_circle = list(filter(lambda p: p[0]**2 + p[1]**2 <= 1, point_list))
print(points_in_unit_circle)
points_with_positive_coordinates = list(filter(lambda p: p[0] > 0 and p[1] > 0, point_list))
print(points_with_positive_coordinates)
sorting_key_y_decr_x_incr = sorted(point_list, key=lambda p: (-p[1], p[0]))
print(sorting_key_y_decr_x_incr)
sorting_key_sum = sorted(point_list, key=lambda p: abs(p[0]) + abs(p[1]))
print(sorting_key_sum)


#Exercise 4.2
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse_range(L, 3, 6)

def reverse_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1
        

def reverse_range(L, left, right):
    reverse_iterative(L, left, right)


print(L)



def reverse_recursive(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_recursive(L, left + 1, right - 1)

def reverse_range(L, left, right):
    reverse_recursive(L, left, right)

print(L)




#Excercise 4.3
def iter_even():
    i = 0
    while True:
        yield i
        i += 2
        
for i in iter_even():
    print(i)
    if i > 100:   
        break
        
def iter_odd():
    n = 1
    while True:
        yield n
        n += 2
        
for n in iter_odd():
    print(n)
    if n > 100:   
        break
        
def iter_power(k):
    s = 1
    while True:
        yield s
        s *= k
for s in iter_power(2):
    print(s)
    if s > 100:   
        break