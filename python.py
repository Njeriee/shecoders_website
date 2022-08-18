print ("big" > "small")
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

print(76+26+21)

x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))

print(0%1)

def sum_divisors(n):
	sum = 0
	divisor = 1
	while divisor < n:
		if (n % divisor == 0):
			sum = sum + divisor
		divisor += 1
	return sum

print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))

for i in range(1,4):
	print (i)

def factorial(n):
    result = 1
    for i in range(1,n+1):
       result = i * (i +1)
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
votes(['yes', 'no', 'maybe'])

for x in range(1, 10, 3):
    print(x)

print(144//10)