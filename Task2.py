name = input("What is your name?")
NummberCookeis = int(input("How many cookeis would you like to have? "))
if NummberCookeis >= 1 and NummberCookeis < 10:
  print ("Hi",name,"\nAre you sure it’s enough?")
  print ("Her are your cookeis:", "cookeis " * NummberCookeis)
elif NummberCookeis >= 10 and NummberCookeis < 20:
  print ("Hi",name,"\nI agree cookies are delicious!")
  print ("Her are your cookeis:", "cookeis " * NummberCookeis)
elif NummberCookeis >= 20 and NummberCookeis < 51:
  print ("Hi",name,"\nBe careful, it’s getting too much")
  print ("Her are your cookeis:", "cookeis " * NummberCookeis) 
elif NummberCookeis > 50:
  print ("Hi",name,"\nNo way, it’s getting too much")
  print ("Her are your cookeis:", "cookeis " * 50) 
else:
  print ("Hi",name,"\nSomething must be wrong, I give you 10 cookies")
  print ("Her are your cookeis:", "cookeis " * 10)