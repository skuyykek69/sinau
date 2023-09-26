bilangan_awal=1
bilangan_akhir=71

for x in range(1, 71+1): #disini juga bisa langsung input bilangan nya misal| for x in range(1, 71+1):
    if x > 1:
        for y in range(2, x):
            if (x % y) == 0:
                break
        else :
            print(x)
