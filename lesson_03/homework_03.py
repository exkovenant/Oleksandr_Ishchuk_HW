

# Task 1
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# Task 2
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

# Task 3
print(alice_in_wonderland)

# Task 4
black = 436402
azov = 37800
total= black + azov
print("Площа Чорного та Азовського морів", total)

# Task 5
all = 375291
first_and_second = 250449
second_and_third = 222950

second = first_and_second + second_and_third - all
first = first_and_second - second
third = second_and_third - second

print("first", first)
print("second", second)
print("third:", third)

# Task 6
month = 1179
all = month * 18
print (all)

# Task 7
a = 8019%8
b = 9907%9
c = 2789%5
d = 7248%6
e = 7128%5
f = 19224%9
print(a, b, c, d, e, f)

# Task 8
Pizza_L = 274 * 4
Pizza_M = 218 * 2
Juce = 35 * 4
Cake = 350
Water = 21 * 3
all = Pizza_L + Pizza_M + Juce + Cake + Water
print(all)

# Task 9
all = 232
list = 8
album = all // list
print(album)

# Task 10
distance = 1600
fuel_per_100 = 9
tank = 48

fuel_needed = distance // 100 * fuel_per_100
refuels = fuel_needed // tank

print("Потрібно бензину:", fuel_needed)
print("Мінімум заправок:", refuels)