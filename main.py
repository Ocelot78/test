from replit import clear
import time 
name = input("Napisz Swój Nick: ")
print("Witaj", name)
time.sleep(3)
clear()
print("Ładowanie...")
pytanie1 = input("Czy grasz w LoL: ")
print("Wpisz z capslokiem TAK LUB NIE")
if pytanie1 == ("TAK"):
  print("Nie będziesz miał dziewczyny")
elif pytanie1 == ("NIE"):
  print("Będziesz miał dziewczyne")