"""CALCULATOR"""


# addition

def add(t1, t2):
    print(f">>> {t1+t2}")


# subtraction

def subtract(t1, t2):
    print(f">>> {t1 - t2}")


# multiplication

def multiply(t1, t2):
    print(f">>> {t1 * t2}")


# division

def divide(t1, t2):
    print(f">>> {t1 / t2}")


# percent

def percent(t, r):
    print(f">>> {(t / r) * 100}")


# exponentiation

def exponent(t, p):
    print(f">>> {t ** p}")


# linear equation
import math


def solve(L1, L2):
    l = list()
    l1_o = L1[0]
    l2_o = L2[0]
    if l1_o[-1] == l2_o[-1]:
        for i in range(len(L1)):
            try:
                Sum = int(L1[i]) + int(L2[i])
                l.append(Sum)
            except ValueError:
                l.append(L1[i])
        ycoeff_i = l.index("y")-1
        yval = l[-1]/l[ycoeff_i]
        print(f"Y value is {yval}")

        rhst = int(L1[-1])

        ycoeff = int(L1[L1.index("y")-1])

        xcoeff = int(L1[0])

        xval = (rhst - yval*ycoeff)/xcoeff
        print(f"X value is {xval}")

    else:
        lex = []
        print(l1_o)
        print(l2_o)
        intingl1 = math.fabs(int(l2_o))
        print(intingl1)
        for i in L1:
            try:
                inting = int(i)*intingl1
                lex.append(inting)
            except ValueError:
                lex.append(i)
        for i in range(len(L1)):
            try:
                Sum = int(L1[i]) + int(L2[i])
                l.append(Sum)
            except ValueError:
                l.append(L1[i])
        print(lex)
        ycoeff_i = l.index("y")-1
        yval = l[-1]/l[ycoeff_i]
        print(f"Y value is {yval}")

        rhst = int(L1[-1])

        ycoeff = int(L1[L1.index("y")-1])

        xcoeff = int(L1[0])

        xval = (rhst - yval*ycoeff)/xcoeff
        print(f"X value is {xval}")


def fix(L1, L2, operation):
    if operation == '+':
        pass
    elif operation == "-":
        for i in L2:
            if i.isdigit():
                index_i = L2.index(i)
                L2[index_i] = f"-{i}"

                if L2[index_i - 1] == "-":
                    L2[index_i - 1] = "+"
                    L2[index_i] = f"{i}"

    for i in L1:
        if i.isdigit():
            index_i = L1.index(i)
            if L1[index_i-1] == "+":
                L1.pop(index_i - 1)
                L1.pop(index_i - 1)
                L1.insert(index_i-1, f"+{i}")
            elif L1[index_i-1] == '-':
                L1.pop(index_i - 1)
                L1.pop(index_i - 1)
                L1.insert(index_i-1, f"-{i}")

    for i in L2:
        if i.isdigit():
            index_i = L2.index(i)
            if L2[index_i - 1] == "+":
                L2.pop(index_i - 1)
                L2.pop(index_i - 1)
                L2.insert(index_i-1, f"+{i}")

            elif L2[index_i - 1] == '-':
                L2.pop(index_i - 1)
                L2.pop(index_i - 1)
                L2.insert(index_i-1, f"-{i}")

    solve(L1, L2)


def eq(eq1, eq2):

    operation, coefficient1a, coefficient2a, coefficient1b, coefficient2b = "", "", "", "", ""
    L1 = list(eq1)
    L2 = list(eq2)
    iy1 = L1.index("y")
    iy2 = L2.index("y")

    if L1[iy1 - 1].isdigit():
        coefficient1b = L1[iy1 - 1]
    else:
        L1.insert(iy1, "1")

    if L2[iy2 - 1].isdigit():
        coefficient2b = L2[iy2 - 1]
    else:
        L2.insert(iy2, "1")

    if L1[0].isalpha():
        coefficient1a = 1
        L1.insert(0, "1")
    else:
        coefficient1a = L1[0]

    if L2[0].isalpha():
        coefficient2a = 1
        L2.insert(0, "1")
    else:
        coefficient2a = L1[0]
        print(coefficient2a)

    if '+' in L1:
        if '+' in L2:
            operation = '-'
        elif '-' in L2:
            operation = '+'
    if '-' in L1:
        if '+' in L2:
            operation = '+'
        elif '-' in L2:
            operation = '-'
    fix(L1, L2, operation)


eq("x-3y=9", "3x-2y=5")

