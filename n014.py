a = int(input())
b = int(input())
if a > b :
    ans = b - (a % b)
elif a == b :
    ans = 0
else :
    ans = b - a
print(ans)
