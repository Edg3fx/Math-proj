# Discriminant method

def solve(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        print("No roots exist for this equation")
    
    elif D == 0:
        result = (-b+D**0.5)/(2*a)
        print(f"This equation has one root - x = {result}")
    
    else:
        result1 = (-b+D**0.5)/(2*a)
        result2 = (-b-D**0.5)/(2*a)
        print(f'This equation has two roots x = {result1}, x = {result2}')

def quad_form(eqn):
    L = eqn.split('x')

    a = int(L[0])
    b = int(L[1][2:])
    c = int(L[2])
    
    solve(a, b, c)

Equation = input("Enter the equation in 'ax^2-bx+c' form\n>>> ")
quad_form(Equation)

# Factorisation method 

def solve(alpha, beta, c, a = 1):
    print(a, alpha, beta, c)
    if alpha/a == c/beta or beta/a == c/alpha:
        root1 = -alpha/a
        print(f'First root is {root1}')
        print(f'{int(alpha/root1)}x+{int(beta/root1)}')
        root2 = -beta/alpha
        print(f"Second root is {root2}")
    # Emil is a nigger
    
 
def roots(Sum, product, a, c):
    print(float(Sum))
    modprod = abs(product)
    for i in range(1, modprod+1):
        if modprod % i == 0:
            fac1 = modprod/i
            fac2 = modprod/fac1
            if product < 0:
                print(f'{fac1} - {fac2} = {fac1-fac2}')
                print(float(Sum))
                if fac1 - fac2 == float(Sum):
                    alpha = int(fac1)
                    beta = int(-fac2)
                    print(f'factors located: {alpha}, {beta}')
                    print(f'Sum is {alpha+beta}, Product is {alpha*beta}')
                    break
    
    
    solve(alpha, beta, c, a)
        

def quad_form(eq):
    L = eq.split("x")
    # print(L)
    Sum = int(L[1][2:])
    Prod = int(L[0])*int(L[2])
    print('Sum = ',Sum, 'Product =', Prod) 
    roots(Sum, Prod, int(L[0]), int(L[2]))

Equation = input("Enter the equation in 'ax^2-bx+c' form\n>>> ")
quad_form(Equation)

