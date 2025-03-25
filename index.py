import sys

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

