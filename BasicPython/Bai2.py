# Tim nghiem x
import math
from sys import flags

def InputData():
    a = float(input("Nhap a="))
    b = float(input("Nhap b="))
    return a,b

def SolveEqual(a,b):
    if a == 0:
        if b == 0:
            print("Vo so nghiem.")
        else:
            print("Vo nghiem.")
    else:
        x = -b/a
        print("Nghiem x=%.31f"%x, end = '\n')

def main():
    a,b = InputData()
    SolveEqual(a,b)
if __name__ == "__main__":
    main()