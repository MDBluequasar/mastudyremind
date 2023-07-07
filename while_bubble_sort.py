
s = [2,3,1,4,6,8,9]
n = 0


while n < len(s):
    m = 0
    while m < len(s) - 1:
        if s[m] > s[m + 1]:
            s[m], s[m + 1] = s[m + 1], s[m]
        m += 1
    n += 1
print(s)