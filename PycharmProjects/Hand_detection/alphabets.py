import time as t


def A():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or j == 4 or i == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def B():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or j == 4 or i == 4 or i == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def C():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or i == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def D():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 1 or i == 4 or j == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def E():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or i == 4 or i == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def F():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or i == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def G():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or i == 4 or (i > 1 and j == 4) or (i == 2 and j > 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def H():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (j == 0 or j == 4 or i == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def I():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or i == 4 or j == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def J():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 2 or (i == 4 and j < 3) or (j == 0 and i > 2)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def K():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (j == 0 or (j > 0 and i + j == 3) or (j > 0 and i - j == 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def L():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 4 or j == 0):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def M():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (j == 0 or j == 4 or (i == j and i < 3) or (i + j == 4 and i < 3)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def N():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (j == 0 or j == 4 or i == j):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def O():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 0 or i == 4 or j == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def P():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or (j == 4 and i < 3) or i == 2 or j == 0):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def Q():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if ((i == 0 and j < 4) or (j == 0 and i < 4) or (i == 3 and j < 4) or (j == 3 and i < 4) or (
                    i == j and i > 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def R():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or (j == 4 and i < 3) or i == 2 or j == 0 or (i == j and i > 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def S():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or i == 4 or i == 2 or (j == 0 and i < 3) or (j == 4 and i > 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def T():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or j == 2):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def U():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 4 or j == 0 or j == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def V():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i - j == 2 or i + j == 6 or (j == 0 and i < 2) or (j == 4 and i < 2)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def W():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (j == 0 or j == 4 or (i == j and i > 1) or (i + j == 4 and i > 1)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def X():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == j or i + j == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def Y():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if ((i == j and i < 3) or (i + j == 4 and i < 3) or (j == 2 and i > 2)):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def Z():
    print(end="\n\n")
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or i == 4 or i + j == 4):
                print("*", end='')
            else:
                print(" ", end='')
        print(end="\n")
    t.sleep(0.2)


def draw(a):
    if(a=="a"):
        A()
    elif(a=="b"):
        B()
    elif (a == "c"):
        C()
    elif (a == "d"):
        D()
    elif (a == "e"):
        E()
    elif (a == "f"):
        F()
    elif (a == "g"):
        G()
    elif (a == "h"):
        H()
    elif (a == "i"):
        I()
    elif (a == "j"):
        J()
    elif (a == "k"):
        K()
    elif (a == "l"):
        L()
    elif (a == "m"):
        M()
    elif (a == "n"):
        N()
    elif (a == "o"):
        O()
    elif (a == "p"):
        P()
    elif (a == "q"):
        Q()
    elif (a == "r"):
        R()
    elif (a == "s"):
        S()
    elif (a == "t"):
        T()
    elif (a == "u"):
        U()
    elif (a == "v"):
        V()
    elif (a == "w"):
        W()
    elif (a == "x"):
        X()
    elif (a == "y"):
        Y()
    elif (a == "z"):
        Z()

