#implement a recursion function to find a factorial of given number
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
n=(int(input("enter the number:"))) 
print(fact(n))
print("the factorial of the given number",n,"is",fact(n))