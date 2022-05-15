


if __name__ == "__main__":
    T = int(input())

    C_list = []
    M_list = []
    Y_list = []
    K_list = []

    flag = 0

    for t in range(T):
        flag = 0
        C_list = []
        M_list = []
        Y_list = []
        K_list = []

        for i in range(3):
            C, M, Y, K = map(int, input().split())
            C_list.append(C)
            M_list.append(M)
            Y_list.append(Y)
            K_list.append(K)
        
        print("Case #" + str(t+1) + ": ", end="")

        C_list.sort()
        M_list.sort()
        Y_list.sort()
        K_list.sort()

        # print("c:", C_list[0])
        # print("m: ", M_list[0])
        # print("y: ", Y_list[0])
        # print("k: ", K_list[0])

        if C_list[0]+M_list[0]+Y_list[0]+K_list[0] < 1000000:
            print("IMPOSSIBLE")
        elif C_list[0]+M_list[0]+Y_list[0]+K_list[0] == 1000000:
            print(str(C_list[0]) + " " + str(M_list[0]) + " " + str(Y_list[0]) + " " + str(K_list[0]))
        else:
            results = [C_list[0], M_list[0], Y_list[0], K_list[0]]
            diff = sum(results) - 1000000
            
            max_item = max(results)
            max_ind = results.index(max_item)

            # first max
            if diff < max_item:
                results[max_ind] = results[max_ind] - diff
            else:
                diff = diff - results[max_ind]
                results[max_ind] = 0
                
                max_item = max(results)
                max_ind = results.index(max_item)

                # second max
                if diff < max_item:
                    results[max_ind] = results[max_ind] - diff
                else:
                    diff = diff - results[max_ind]
                    results[max_ind] = 0

                    max_item = max(results)
                    max_ind = results.index(max_item)

                    # third max
                    if diff < max_item:
                        results[max_ind] = results[max_ind] - diff
                    else:
                        diff = diff - results[max_ind]
                        results[max_ind] = 0

                        max_item = max(results)
                        max_ind = results.index(max_item)

                        # forth max
                        if diff < max_item:
                            results[max_ind] = results[max_ind] - diff
                        else:
                            print("IMPOSSIBLE")

            print(str(results[0]) + " " + str(results[1]) + " " + str(results[2]) + " " + str(results[3]))


                

                    


