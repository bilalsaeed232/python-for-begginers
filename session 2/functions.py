# python builtin functions

# print("hello world")
# range(10)


# user defined functions
# e.g table(3)

# function defining
# function syntax
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


# function calling
table(30)


print("blabalala")
print("blabalala")


table(7)
table(6)
table(13)

table(2)

table(0)
