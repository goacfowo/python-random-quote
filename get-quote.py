import random

def get():
  file = open("quotes.txt", "r")
  quotes = file.readlines()
  file.close()
  first = 0
  last = len(quotes) - 1
  rnd = random.randint(first, last)
  print(quotes[rnd], end="")

def add():
  file = open("quotes.txt", "a")
  quote = str(input(">>> "))
  file.write(quote)
  file.close()

if __name__== "__main__":
  mode = str(input("Would you like to get or add a quote? (G/a) ").lower() or "g")
  if mode == "g":
    get()
  elif mode == "a":
    add()
  else:
    print("Error: undefined input.")
