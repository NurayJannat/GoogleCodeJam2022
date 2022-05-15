def row_gen(i, n_col):
    if i%2==0:
        symb = ["+","-"]
    else:
        symb = ["|", "."]

    row_result = ''

    for j in range(n_col):
        if (j == 0 or j == 1) and (i == 0 or i == 1):
            row_result = row_result + "."
        elif j%2 == 0:
            row_result = row_result + symb[0]
        else:
            row_result = row_result + symb[1]

    
    return row_result


def mat_gen(t, R, C):
    n_row = 2*R + 1
    n_col = 2*C + 1

    mat_result = []
    
    print("Case #" + str(t+1) + ":")

    for i in range(n_row):
        row_result = row_gen(i, n_col)
        mat_result.append(row_result)
        print(row_result)


if __name__=="__main__":
    T = int(input())
    
    for t in range(T):
        R, C = map(int, input().split())
        R = int(R)
        C = int(C)
        mat_gen(t, R, C)

    


