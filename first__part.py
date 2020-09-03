
import camelcase
import re
import math

#Python String Formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


#Python User Input
username = input("Enter username:")
print("Username is: " + username)

#Exception Handling

try:
  print(x)
except:
  print("An exception occurred")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

#Python PIP
c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

#RegEx Module
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Python JSON
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Python Math
#The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x) #5
print(y) # 25


x = abs(-7.25)

print(x)

#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)

print(x)
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#Python Datetime
#import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)

print(x)

#What is a Module?
#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)

#Use a Module
import mymodule

mymodule.greeting("Jonathan")


#Python Scope

def myfunc():
  x = 300
  print(x)

myfunc()

#The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#Python Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


