from sympy import *

def main():
    print("input pointer :")
    dot1 = input()

    print("input pointer :")
    dot2 = input()

    print("input pointer :")
    dot3 = input()

    x0 = int(dot1.split(",")[0])
    y0 = int(dot1.split(",")[1])

    x1 = int(dot2.split(",")[0])
    y1 = int(dot2.split(",")[1])

    x2 = int(dot3.split(",")[0])
    y2 = int(dot3.split(",")[1])

    x = Symbol('x')
    P0 =  expand((x-x1)*(x-x2)) * ( y0 / ((x0-x1)*(x0-x2)))
    P1 =  expand((x-x0)*(x-x2)) * ( y1 / ((x1-x0)*(x1-x2)))
    P2 =  expand((x-x0)*(x-x1)) * ( y2 / ((x2-x0)*(x2-x1)))
    result = P0+P1+P2
    pprint(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
