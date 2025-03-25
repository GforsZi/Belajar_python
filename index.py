import sys
import random

print(sys.version)

name = ["Givaldi", "Andi", "Dion"]
umur = 5 + 7
print("Hello " + name[1] + " Anda berumur", umur, "tahun")
if umur > 10:
  print(name[1] + " ternyata anda sudah besar")
else:
  print(name[1] + " anda berjiwa muda")

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
print(listPerson[0]["name"])

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