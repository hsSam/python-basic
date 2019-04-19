print("hello")

# basic value & tab
# Y= 3
x = 23
if x == 2:
    print("x == 2")
else:
    print("x != 3")

# type list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4, 5]
list3 = ["aa", 2, "cc", 4]
print("list1[0]: ", list1[0])
print("list2[1:3]: ", list2[1:3])

# type dict
nameBook = {"Name": "Alex", "Age": 7, "Class": "First"}
print(nameBook["Name"])
print(nameBook['Age'])
print(nameBook)
# with key & value
for key, value in nameBook.items():
    print(key, " : ", value)
# only value
for value in nameBook:
    print(value)

# while
count = 0
while count < 1:
    print(list2[count])
    count += 1


# def function
def calulus(x):
    y = x + 1
    return y

# def function multi arg
def str_concat (str1, str2):
    result = str1 + " " + str2
    return result


result = calulus(2)
print('calulus :', result)

result = str_concat("apple", "banana")
print('str_concat :', result)


# def class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


obj1 = Person('santos', 18)
obj1.detail()


# def class extend
class Animal:
    def eat(self):
        print('%s eat' %self.name)
    def drink(self):
        print('%s drink' %self.name)
    def shit(selfs):
        print("%s shit" %self.name)
    def pee(self):
        print("%s pee" %self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def cry(self):
        print('cat cry')


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def cry(self):
        print('dog cry')


c1 = Cat("black cat")
c1.eat()
c1.cry()

c2 = Dog('yellow dog')
c2.eat()
c2.cry()

