R, C, M = map(int, input().split(' '))
tmp_arr = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    tmp_in = input().split(' ')
    for j in range(C):
        tmp_arr[i][j] = int(tmp_in[j])
tmp = input().split(' ')
for i in range(M):
    if tmp[i] == '1':
        for j in range(R // 2):
            for k in range(C):
                tmp_arr[j][k], tmp_arr[R - j - 1][k] = tmp_arr[R - j - 1][k], tmp_arr[j][k]
    else:
        tmp_tmp_arr = [[0 for _ in range(R)] for _ in range(C)]
        for j in range(C):
            for k in range(R):
                tmp_tmp_arr[j][k] = tmp_arr[R-k-1][C-j-1]
                R, C = C, R
                tmp_arr = tmp_tmp_arr

print(R, C)
for i in range(R):
    for j in range(C):
        print(tmp_arr[i][j], end=' ')
    print()