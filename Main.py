# for loop demonstration

magicians = ["awais", "mubashir", "sameer", "adeel"]

# prints all items in a list
for magician in magicians:
    print(magician)

cats = ["persian", "british short hair", "domestic", "austrian"]
for cat in cats:
    print(cat + ", is a awesome cat breed")

# a short exercise
pizzas = ["supersupreme", "pepperoni", "foursquare", "jamaican", "spicy hot"]
for pizza in pizzas:
    print(pizza.title())

for pizza in pizzas:
    print("i like " + pizza.title() + " pizza")

print("i like super supreme pizza very much because it contains tender beef cubes,  "
      "\npepperoni slices and tasty cheese")

# range function to print number within a range. last no. doesn't prints
for value in range(1, 11):
    print(value)

# to store range of numbers in a list
numbers = []
for number in range(1, 11):
    numbers.append(number)

print(numbers)

# alternative wrap it in list(range(obj, obj))
numbers = list(range(1, 11))
print("alternative: " + str(numbers))

# using range() with jump/skip.
# following prints even numbers fro 2-10
evenNumbers = list(range(2, 11, 2))
print("Even numbers: " + str(evenNumbers))

# first 10 square numbers using range
squareNumbers = []
for number in range(1, 11):
    squareNumbers.append(number ** 2)

print("First 10 square numbers: " + str(squareNumbers))

# first 10 square numbers using list comprehensions.
# todo: it is standard approach for list operations. steps:
#  1- make expression of values to be added in list.
#  2- make for loop to generate numbers

squareNumbers = [value ** 2 for value in range(1, 11)]
print("First 10 square numbers using comprehension: " + str(squareNumbers))

# simple statistics with number list
myNumbers = [10, 30, 45.6, 99.0, 69, 34.33]
print("smallest number in list: " + str(min(myNumbers)))

print("largest number int list: " + str(max(myNumbers)))

print("sum of all numbers in list: " + str(sum(myNumbers)))

# todo: exercises
# printing 1-1M numbers
# for num in range(1, 1000001):
#     print(num)

# sum of 1M numbers
print("sum of 1M numbers: " + str(sum(range(1, 1000001))))

# multiple of 3s list
threeMultiples = [value * 3 for value in range(3, 31)]
print("multiples of three from 3-30: " + str(threeMultiples))

# first 10 cubes
cubes = [value ** 3 for value in range(1, 11)]
print("First 10 cubes: " + str(cubes))

# slicing the list. ie. getting specific range of items from list.
# last value is not printed so do range + 1 instead.
players = ["afridi", "horse", "umer akmal", "babar azam"]
print(players[1:3])

# automatically starts from beginning of list
print(players[:3])

# automatically ends at end of list
print(players[2:])

# to print last 3 elements
print(players[-3:])

# looping through sliced list (first 3 elements)
for player in players[:3]:
    print(player)

# copying from list
myFavoriteFoods = ["albaik", "shawarma", "biryani", "burger"]
myFriendsFavoriteFoods = myFavoriteFoods[:]  # [:] copies all items from list

print(myFavoriteFoods)
print(myFriendsFavoriteFoods)

myFavoriteFoods.append("karahi")
myFriendsFavoriteFoods.append("ice cream")

print(myFavoriteFoods)
print(myFriendsFavoriteFoods)

# list within a list
lists = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [33.4, 1.30, 4.50, 6.69]]
for list1 in lists:
    print(list1)


# tuples
# Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.
# we use () instead of [] to define tuples

myList = (1, 2, 3, 4, 5)
# myList[0] = 10 --> error. you cannot change tuple

# however you can change the tuple list itself
myList = (1, 3, 5, 7, 9)