import math
def prime(x):
    if x==1 :
        return False
    elif x==2 or x==3:
        return True
    else :
        xSqrt=int(math.sqrt(x))
        for i in range(2,xSqrt+1):
            if x%i==0:
                break
        else:
            return True
    return False

def monisen(x):
    excel=[]
    for i in range(2,1000):
        if prime(i):
            excel.append(i)
    ans=0
    while x>0:
        for i in excel:
            if x==0:
                break
            if prime(2**i-1):
                ans=2**i-1
                x-=1
    else :
        return ans


def main():
    print(monisen(int(input())))
    

if __name__ == "__main__":
    main()