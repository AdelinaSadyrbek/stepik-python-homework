a = int(input('Enter the length of first side'))
b = int(input('Enter the length of second side'))
c = int(input('Enter the length of third side'))
p = (a + b + c)/2
S = p * (p - a) * (p - b) * (p - c)
S2 = S ** 0.5
print(S2)