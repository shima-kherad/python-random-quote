def myfunction():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
__name__ = "myfunction"
if __name__== "myfunction":
  myfunction()
