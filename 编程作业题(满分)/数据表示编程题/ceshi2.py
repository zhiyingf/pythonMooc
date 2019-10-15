def pandigital(nums):
    nlen=len(nums)
    nint=[int(i) for i in nums]
    nint.sort()
    mat=[i for i in range(1,nlen+1)]
    if nint==mat:
        return True
    else :
        return False
def main():
    strs=input().split(',')
    flag=True
    for str1 in strs:
        if pandigital(str1):
            print(str1)
            flag=False
    if flag:
        print('not found')
if __name__ == "__main__":
    main()

