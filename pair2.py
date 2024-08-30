def 중복제거(arr):
    return list(set(arr))

def 합집합(arr1,arr2):
    return list(set(arr1) | set(arr2))

def 교집합(arr1,arr2):
    return list(set(arr1) & set(arr2))


arr1 = [1,1,2,3,4,4,5]
arr2 = [1,3,3,3,3,5]
print(중복제거(arr1))
print(중복제거(arr2))
print(합집합(arr1,arr2))
print(교집합(arr1,arr2))
