def table(n):
  if n == 2:
    print("passa mara 2 table am darla na darzi")
    return

  if n == 0:
    print("invalid number:",n)
    return

  print("***************")
  for i in range(10):
    i = i + 1
    x = i * n
    print(n, "x",i, "=", x)



num = input("Which table? ")
num = int(num)

# while loop runs indefinetly
while num != 0: 
  table(num)
  num = input("Which table? ")
  num = int(num)

