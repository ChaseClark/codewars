def missingNumber(a, N):
    hash_map = [0] * (N + 1)

    for i in range(N - 1):
        hash_map[a[i]] += 1

    for i in range(1, N + 1):
        if hash_map[i] == 0:
            return i

    return -1


N = 5
a = [1, 2, 4, 5]
ans = missingNumber(a, N)
print("The missing number is:", ans)
