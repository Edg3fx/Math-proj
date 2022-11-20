# def equation(eq):

#     sign = eq.index("x")+1
#     op = eq.index("=")
#     a = int(eq[:sign-1])
#     b = int(eq[sign+1:op])
#     c = int(eq[op+1:])


#     if eq[sign] == '+':
#         rhst = c-b
#     else:
#         rhst = c+b

#     rhst/=a
#     print(f'x={rhst}')

# eq = input("Enter the equation\n>>> ")
# equation(eq)



# Linear Equation New

def calc(A1, B1, C1, A2, B2, C2):

    xcoeff = B1*C2-(B2*C1)
    ycoeff = C1*A2-(C2*A1)
    cterm = A1*B2-(A2*B1)

    if cterm == 1 or cterm == -1:
        print("Proceeding swiftly...")
        ax = xcoeff*cterm
        by = ycoeff*cterm
        print(f"x = {ax}")
        print(f"y = {by}")
    else: 
        print("This gonna be long...")
        ax = xcoeff/cterm
        by = ycoeff/cterm
        print(f"x = {ax}")
        print(f"y = {by}")


def coeff(EQ1, EQ2):

    sign1 = EQ1.index("x")+1; sign2 = EQ2.index("x")+1
    op1 = EQ1.index("="); op2 = EQ2.index('=')

    a1 = int(EQ1[:sign1-1])
    b1 = int(EQ1[sign1+1:op1-1])
    c1 = int(EQ1[op1+1:])
    a2 = int(EQ2[:sign2-1])
    b2 = int(EQ2[sign2+1:op2-1])
    c2 = int(EQ2[op2+1:])

    if EQ1[sign1] == '-':
        b1 = -b1
    if EQ2[sign2] == '-':
        b2 = -b2

    if str(c1)[0].isdigit():
        c1 = -c1
    else:
        c2 = c2*-1
    if str(c2)[0].isdigit():
        c2 = -c2
    else:
        c2 = c2*-1

    calc(a1,b1,c1,a2,b2,c2)

eq1 = input("Enter the first equation\n|> ")
eq2 = input("Enter the second equation\n|> ")

coeff(eq1,eq2)
