import random as abacate

sortedNumber_List = []
person_list = []
correct_values = []

for i in range(10):
    randomNumber = abacate.randint(0,100)
    print(randomNumber)
    print("What number you want to try from 0 to 100?")
    try:
        number = int(input())
    except ValueError:
        print('Type a valid value please')
    person_list.append(number)
    sortedNumber_List.append(randomNumber)
    if number in sortedNumber_List:
        correct_values.append(number)

print(sortedNumber_List)
print(person_list)
print(correct_values)