def changeValue(a): # 값
    a = 5

def changeRef(a): # 주소
    a[0] = 5

if __name__ == '__main__':
    a = 0
    arr = [0]
    
    print(a)
    print(arr)
    
    changeValue(a)
    changeRef(arr)
    
    print(a)
    print(arr)
    
    # 기본형은 value
    # 배열 이후에 배운것 Ref