fruits = ['apple', 'bananas', 'cherry', 'kiwi']
animals = ['dog', 'cat','lion']

for f in fruits:
    print(f)

for a in animals:
    print(a)

#O (2 + F + A)

print('----------------')
for a in animals:
    for f in fruits:
        print(f'{a} eats {f}')


num = len(animals)
while num >0:
    print(num)
    num -= 1
    for f in fruits:
        print(f'{num} ----> {f}')
    for a in animals:
        print(f"{num} ----> {a}")
#O(A * (F + A)) => O(AF + A**2)



