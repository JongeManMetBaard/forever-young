tafel = int(input("Welk tafel wilt u zien?"))

for i in range (1,11):
    import time
    t = 0.7
    time.sleep(t)
    print(i, " x ",tafel," =", i*tafel)   