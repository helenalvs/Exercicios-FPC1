Xa0, Ya0, Xa1, Ya1 = list(map(int, input().split()))
Xb0, Yb0, Xb1, Yb1 = list(map(int, input().split()))
if Xa0 > Xb1 or Xa1 < Xb0:
    print(0)
else:
    if Ya0 > Yb1 or Ya1 < Yb0:
        print(0)
    else:
        print(1)