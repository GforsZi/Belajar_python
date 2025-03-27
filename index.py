import sys
import random
import myModule
import datetime
import platform
import math
import json
import re


print(sys.version)

name = ["Givaldi", "Andi", "Dion"]
umur = 5 + 7
print("Hello " + name[1] + " Anda berumur", umur, "tahun")
if umur > 10:
  print(name[1] + " ternyata anda sudah besar")
else:
  print(name[1] + " anda berjiwa muda")

phone_name, phone_ram, phone_lcd = "redmi", "grey", "amoled"
player1, player2, player3 = name

print("Hallo nama saya " + player2 + " dan saya memiliki hp "
 + phone_name +  " dengan ram " + phone_ram + " ditambah layanya juga " + phone_lcd)

num, flt, complx = 10, 1.67, 1j
print(type(num))
print(type(flt))
print(type(complx))

print(random.randrange(1, 100))

text = "hello python"
print(len(text))
print("hello" in text)

if "python" not in text:
  print("you're right")
else:
  print(" you're wrong ")

print(text[6:12])

tittle = "MY, COol, world"

print(tittle.upper())
print(tittle.lower())
print(tittle.strip())
print(tittle.replace("COol", "amazing"))
print(tittle.split(","))

print(f"my name {player3} and i have {umur:.2f}")

name.insert(0, "Aldo")
name.append("Nabil")
cash = ["2000", "3000", "5000"]
cash.extend(name)
print(cash)
name.remove("Givaldi")
name.pop()
del name[0]
cash.clear()
print(cash)
print(name)

print("---")

color = ["blue", "red", "cyan", "yellow"]
for i in range(len(color)):
  print(color[i])

print("---")

[print(x) for x in color]

print("---")

newColor = [i.upper() for i in color if i != "yellow"]
newColor.sort(reverse=True)
print(newColor)

secondColor = newColor.copy()
print(secondColor)

secondColor.extend(color)
print(secondColor)

print("---")

mytuple = ("apple", "banana", "cherry")
yourtuple = ("manggo",)
mytuple += yourtuple
print(mytuple)

(apple, banana, cherry, manggo) = mytuple
print(apple)

print("---")

thisset = {"apple", "banana", "cherry", "apple"}
leght = {"long", "sort"}
thisset.add("starfruit")
thisset.update(leght)
print(thisset)
thisset.discard("banana")
print(thisset)
secondset = {"high", "low", "mid"}
newset = thisset.union(leght, secondset)
print(newset)

print("---")

listPerson = [
  {
  "name": "Gival",
  "cash": 1000,
  "cool": True
  },
  {
  "name": "chino",
  "cash": 1500,
  "cool": True
  },
]

listPerson[0].update({"cool": False})
listPerson[1].update({"pretty": True})
listPerson[1].pop("cool")

for x in listPerson:
  print(x)

myFamily = {
  "family": listPerson,
}
print(myFamily)

print("---")

a, b = 1, 5
if a > b: print("yes")
else: print("no")

print("a") if a > b else print("b")

print("---")

while a <= 10:
  print(a)
  a += 1
else:
  print("i more than 10")

print("---")

for x in "yahahai":
  print(x)
else:
  print("yahahai is end")

print("---")

def sayHello(*subject):
  print("hallo " + subject[0])

sayHello("python", "world" )

def sayRole(**role):
  print("hey there are officer " + role["police"])

sayRole(police = "jeb", teacher = "elsa")

def calculation(x, y, operation):
  if operation == "+":
    return x + y
  elif operation == "-":
    return x - y
  elif operation == "*":
    return x * y
  elif operation == "/":
    return x / y
  else:
    return "operation failed"

print(calculation(5, 6, "/"))

print("---")

myCash = lambda x : x * 3
print(myCash(6))

print("---")

class person:

  def __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job
  
  def __str__(self):
    return f"Name: {self.name}, Age: ({self.age}), Major: {self.job}"

  def sayHello(self):
    print("Hallo my name is " + self.name)

c1 = person("Gival", 17, "Web developer")
c1.sayHello()
print(c1)

print("---")

class friend(person):
  def introduce(self):
    print("Hallo saya " + self.name + "Salam kenal")

c2 = friend("chino", 13, "barista")
c2.sayHello()
c2.introduce()
print(c2)

print("---")

myiter = iter(mytuple)
print(next(myiter))

class numberOfCash:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

c3 =numberOfCash()
numberIter = iter(c3)
print(next(numberIter))

for x in numberIter:
  print(x)

print("---")

print(len(c2.name))

class partner(person):
  pass

c4 = partner("zblazer", 12, "gamer")
c4.sayHello()

print("---")

myModule.sayMyName("Givaldi")

os = platform.system()
print(os)

print(datetime.datetime.now().strftime("%A"))

print(datetime.datetime(2020, 10, 5).strftime("%B"))

print("---")

print(min(5, 10, 25))
print(max(5, 10, 25))
print(abs(-7.25))
print(pow(4, 3))
print(math.sqrt(64))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)

print("---")

obj_str = '{ "name":"Chino", "age":13}'
myjson = json.loads(obj_str)
print(myjson["name"])

print(json.dumps(myjson))

print("---")

txt = "The rain in Spain"
search = re.search("^The.*Spain$", txt) 
print(type(search))

print("---")

def writeToPaper(text):
  try:
    f = open("paper.txt", "a")
    f.write("")
    try:
      f.write(text)
      print(f"{text} sudah berhasil di tulis ke paper.txt")
    except:
      print("format text tidak valid")
    finally:
      f.close()
  except:
    print("terjadi kesalahan pada system") 

writeToPaper(" akhirnya menamatkan python dasar! ")

print("---")

username = input("Masukan username:")
print("Terimakasih " + username + " sudah menjalankan file belajar python dasar milik saya")

print("---")

print("chapter belajar dasar python tamat!")