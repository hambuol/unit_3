# written by oliver hamburger
# program takes coefficients of quadratic formula and prints zeros

#imports cmath
import cmath

def printinstructions():
    '''prints what this program does '''
    print("this program will calculate the roots")
    print(" of a quadratic equation. please type in the coefficients")
    print(" a, b, and c and the roots of the equation will be displayed.")

def getfirstcoefficient():
    '''returns the first coefficient in a quadratic equation'''
    a = float(input("a: "))
    return a

def getsecondcoefficient():
    '''returns the second coefficient in a quadratic equation'''
    b = float(input("b: "))
    return b

def getthirdcoefficient():
    '''returns the third coefficient in a quadratic equation'''
    c = float(input("c: "))
    return c

def calculateroots(a, b, c,):
    '''calculates the roots of the three coefficients with the quadratic equation'''
    root_1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    root_2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("the first root is: ", root_1)
    print("the second root is: ", root_2)

#function that runs all the other functions in order
def main():
    printinstructions()
    a = getfirstcoefficient()
    b = getsecondcoefficient()
    c = getthirdcoefficient()
    calculateroots(a, b, c,)


#calls the function that runs all the other function
main()

