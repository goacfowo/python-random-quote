import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  first = 0
  last = len(quotes) - 1
  rnd = random.randint(first, last)
  
  print(quotes[rnd])

if __name__== "__main__":
  primary()
