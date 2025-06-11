A = int(input('Enter minimum recommended sleep hours'))
B = int(input('Enter maximum recommended sleep hours'))
H = int(input('Enter actual sleep hours7'))
if A <= H <= B:
    print('normal')
elif H <= A:
    print('not enough')
else:
    print('too much')