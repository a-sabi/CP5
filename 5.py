while True:
    try:
        A = int(input("Введите натуральное число A:"))
        if A <= 0:
            raise Exeption()
        D = int(input("Введите натуральное число D:"))
        if D <= 0:
            raise Exeption()
    except:
        print("Введено не натуральное число")
        continue
    else :
        if(A * (2)**0.5 <= D):
            print("YES")
        else:
            print("NO") 
        break     