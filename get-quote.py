import random


def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt","r")
  quotes = f.readlines()

  #f.writelines(["\nSee you soon!", "\nOver and out."])
 
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  #print(quotes)
  print(quotes[rnd:rnd+2])
  f.close()



if __name__== "__main__":
  primary()
