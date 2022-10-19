from replit import clear
import time 
name = input("Napisz Swój Nick: ")
print("Witaj", name)
time.sleep(3)
clear()
print("Ładowanie...")
time.sleep(3)
print("Wpisz capslokiem TAK LUB NIE ")
pytanie1 = input("Czy grasz w LoL: ")
if pytanie1 == ("TAK"):
  clear()
  print("Nie będziesz miał dziewczyny")
elif pytanie1 == ("NIE"):
  clear()
  print("Będziesz miał dziewczyne")