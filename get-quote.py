def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

__name__ == "__main__"  
if __name__== "__main__":
  main()
