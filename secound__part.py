class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


# Array
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")

#Python Lambda
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#python_functions
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def myfunction():
  pass

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#Python While Loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Else if 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Program to demonstrate conditional operator 
a, b = 10, 20

# Copy value of a in min if a < b else copy b 
min = a if a < b else b 

print(min) 


# Python program to demonstrate ternary operator 
a, b = 10, 20
  
# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 
  
# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 
  
# lamda is more efficient than above two methods 
# because in lambda  we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]())


#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#https://www.w3schools.com/python/python_dictionaries.asp


###Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

#remove bananna 
thisset.discard("banana")
#clear the set
thisset.clear()
#del thisset
del thisset


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#https://www.w3schools.com/python/python_sets.asp
# last where I was 