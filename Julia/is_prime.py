from math import sqrt
def is_prime(n):
	if n<= 3:
		return True
	if n%2 == 0:
		return False
	for i in range(3,sqrt(n),2):
		if n%i==0:
			return False
	return True

print(is_prime(100))