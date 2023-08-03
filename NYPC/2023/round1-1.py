arr1 = [];arr2 = []
N = int(input())
for _ in range(N):
    arr1.append(input())
K = int(input())
for _ in range(K):
    arr2.append(input())
_arr1 = sorted(list(set(arr1)))
_arr2 = sorted(list(set(arr2)))
result_arr = [item for item in _arr1 if item not in _arr2]
print(len(result_arr))
for i in range(len(result_arr)):print(result_arr[i])