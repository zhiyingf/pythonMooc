def find_person(dict,name):
    s1=dict.get(name)
    if s1==None:
        print('Not Found')
    else:
        print(s1)
def main():
    dict={'xiaoyun':'88888','xiaohong':'5555555','xiaoteng':'11111','xiaoyi':'12341234','xiaoyang':'1212121'}
    find_person(dict,input())
if __name__ == "__main__":
    main()