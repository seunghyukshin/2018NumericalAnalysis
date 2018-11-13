from sympy import *

def main():
    print("input pointer :")
    dot1 = input()

    print("input pointer :")
    dot2 = input()

    print("input pointer :")
    dot3 = input()

    print("input pointer :")
    dot4 = input()

    x0 = int(dot1.split(",")[0])
    y0 = int(dot1.split(",")[1])

    x1 = int(dot2.split(",")[0])
    y1 = int(dot2.split(",")[1])

    x2 = int(dot3.split(",")[0])
    y2 = int(dot3.split(",")[1])

    x3 = int(dot4.split(",")[0])
    y3 = int(dot4.split(",")[1])

    x = Symbol('x')

    dy1 = (y1-y0) / (x1-x0)
    dy2 = (y2-y0) / (x2-x0)
    dy3 = (y3-y0) / (x3-x0)
    d2y2 = (dy2 - dy1) / (x2-x1)
    d2y3 = (dy3 - dy1) / (x3-x1)
    d3y3 = (d2y3 - d2y2) / (x3-x2)

    result = y0 + dy1*(x-x0) + d2y2*expand((x-x0)*(x-x1)) + d3y3*expand((x-x0)*(x-x1)*(x-x2))
    pprint(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
