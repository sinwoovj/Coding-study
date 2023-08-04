def generate_binary_strings(n):
    result = []
    
    def generate_binary_string(current, length):
        if length == 0:
            result.append(current)
        else:
            generate_binary_string(current + "0", length - 1)
            generate_binary_string(current + "1", length - 1)
    
    generate_binary_string("", n)
    return result

def cal(i, x, K):
    return (x + 1) % (2 ** K) if i == 0 else (x * 2) % (2 ** K)

def min_operations(x, cnt, K):
    binstr = generate_binary_strings(cnt)
    for i in range(len(binstr)):
        if m(x, binstr[i], 0, len(binstr[i]), K):
            return cnt
    return min_operations(X, cnt + 1, K)

def m(x, i, st, ed, K):
    if x == 0:
        return True
    if st == ed:
        return False
    else:
        return m(cal(int(i[st]), x, K), i, st + 1, ed, K)

K = int(input())
X_binary = input()
X = int(X_binary, 2)
if X == 0:
    print(0)
else:
    print(min_operations(X, 1, K))
