N=int(input())
count=1
money=0
while count<=N :
    ans=count*10000*(1/N)
    money += ans
    count += 1 #countを1増やす
#出力
print(format(money))
