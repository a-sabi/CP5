while True:
    try:
        A = int(input("Введите натуральное число A:"))
        D = int(input("Введите натуральное число D:"))
        if A<0 or D<0:
            raise Exeption()
    except :
        continue
    else :
        if(A * (2)**0.5 <= D):
            print("YES")
        else:
            print("NO") 
        break     