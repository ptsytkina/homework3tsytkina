#1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 101]

print(sum(numbers))


# #2

import math as m
print(min(numbers))

# #3

print(list(reversed(numbers)))

#4

for i in numbers:
    if i%2 != 0:
        print(i)

#5

mnozhnyk = 10

for i in numbers:
    print(i*mnozhnyk)

#6

x = int(input("vvedit` x:"))
filtered = []

for i in numbers:
    if i<x:
        filtered.append(i)

if filtered:
    print(max(filtered))

else:
    print("vidsutne")

#7

numbers_positive = [n for n in numbers if n>0]


if numbers_positive:
    average_positive = sum(numbers_positive)/len(numbers_positive)
    print(average_positive)
else:
    print("no positive numbers, or they = 0")

#8

y = int(input("vvedit y"))
listik = []

for i in numbers:
    if i%y == 0:
        listik.append(i)
print(sum(listik))

#9

kvadratiki = [i**2 for i in numbers]

print(kvadratiki)

#10

dodatni = []

for i in numbers:
    if i > 0:
        dodatni.append(i)

print(dodatni)

#11

list_for_prefix = ["розлогий" , "пречудовий", "розрісся", "розлюбити", "прекрасний"]

prefix = "роз"

obrani_znachennia = [s for s in list_for_prefix if s.startswith(prefix)]

print(obrani_znachennia)

#12

N = int(input("put n"))

if N>len(numbers):
    print("zabahato")
else:
    print(sum(numbers[:N]))

# 13

list_for_palondromy = [121, 222, 404, 58309, 2785, 55, 1000]

palindromes = [i for i in list_for_palondromy if str(i) == str(i)[::-1]]

print(palindromes)

#14

dilnyk = int(input("vvedit dilnyk"))

znachennya = [i % dilnyk == 0 for i in numbers]

print(znachennya)

#15

#Фільтрувати за кількома умовами: числа, які діляться на X, але не діляться на Y

X = int(input("cyfra 1"))
Y = int(input("cyfra 2"))

list_55 = []

for i in numbers:
    if i%X==0 and i%Y != 0:
        list_55.append(i)

print(list_55)

##16

#Зведення вкладених списків: зведення списку списків в єдиний список.

list_pro_max = [numbers , list_for_prefix]

list_pro_max_filtered = sum(list_pro_max, [])

print(list_pro_max_filtered)

##17

listik_for_upper_lower = ["Odyn Dva trZHy chtery"]

upper_chars = [char for word in listik_for_upper_lower for char in word if char.isupper()]

riadki = [s for s in upper_chars]

print(riadki)

#18
list_for_count = [55, 3545, 11938, 55, 55, 6, 6, 6, 7, 29, 24, 484]


from collections import Counter

chastota = Counter(list_for_count)


def sorting(x):
    return (-x, -chastota[x])

sorted_listik = sorted(list_for_count, key=sorting)

print(sorted_listik)
    


        

#19

ab = [5, 8, 5, 9]
bc = [9, 6, 3, 2]
dc = []

if len(ab) == len(bc):
    for a, b in zip(ab, bc):
        if a>b:
            dc.append((a,b))

print(dc)

#20

slovnyk = {
    "Zarplata 1" : 2948 ,
    "Zarplata 2" : 3478873, 
    "Zarplata 3" : 4373457835478
}


suma = sum(slovnyk.values())

print(suma)

#21

new_numbers = [55 if n<55 else n for n in numbers]

print(new_numbers)

#22

dovzhyna = int(input("dovzhyna"))
count_dovzhyna = 0

for s in list_for_prefix:
    if len(s)>dovzhyna:
        count_dovzhyna+=1

print(count_dovzhyna)

#24

chyslo_1 = int(input("vvedit chyslo:"))
pomnozheni = []
y_1 = 5

for num in numbers:
    if num>chyslo_1:
        pomnozheni.append(num*y_1)

print(pomnozheni)

#23

list_a = [1, 2, 3, 4, 5]

list_b = ["a", "b", "c", "d", "e"]

obiednannia = []

for a, b in zip(list_a, list_b):
    obiednannia.append(a)
    obiednannia.append(b)

print(obiednannia)