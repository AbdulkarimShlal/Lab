num = int(input("How many numbers do you have? "))
x = 0
n = 0
while x < num:
  x = x+1
  print ("What is the", x ,"nummber?")
  n1 = int(input())
  n = n + n1 
print("The avreage is:",n/x)