import random
def myfunction():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 13
  rnd = random.randint(0, last) 
  print(quotes[rnd])
__name__ = "myfunction"
if __name__== "myfunction":
  myfunction()
