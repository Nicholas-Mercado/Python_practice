

arr1 = [1, 2, 3, 4, 5, 6, 7, 8,88,92,33]
arr2 = [1, 2, 7, 8, 5, 22,33,55,88]


def doescontain(arry_1, arry_2):

    larrdict = dict.fromkeys(arry_1, True)
    # larrdict = arry_1
    arr3 = []
    inc = 0
    
    for x in arry_2:
        if larrdict.get(x):
            inc+=1
            print(x)
            arr3.append(x)
        else:
          inc+=1
    # for x in arry_2:
    #   if x in larrdict:
    #     arr3.append(x)
    #     inc+=1
    #   else:
    #     inc+=1
    print(arr3,inc)
    
# print(set(arr1) & set(arr2))   
    

doescontain(arr1, arr2)
