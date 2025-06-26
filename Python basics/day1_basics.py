#i/o
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"Hello {name}, you are {age} years old\n\n")

#loop
for i in range(1, 101):
  print(i, end = " , ")
print("\n\n")

#factorial
def factorial(n: int) -> int:
  if n == 0 or n == 1:
    return n
  else: 
    return n * factorial(n-1)

n = int(input("Enter number: "))
print(f"{n}! = {factorial(n)}")
print("\n")

#Counter
freq = dict()
list = [87, 43, 29, 61, 98, 54, 70, 36, 15, 88, 7, 40, 65, 91, 53, 85, 1, 24, 99, 32, 57, 20, 39, 2, 62, 28, 95, 60, 5, 33, 76, 74, 12, 13, 45, 59, 8,    
        25, 11, 90, 34, 78, 50, 10, 96, 92, 19, 6, 17, 69]
for x in list:
  if x not in freq:
    freq.update({x: 1})
  else: 
    freq[x] += 1
print(freq)
