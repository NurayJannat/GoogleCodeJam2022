
T = int(input())

for t in range(T):
    N = int(input())
    dices = input().split()
    dices = [int(d) for d in dices]
    
    dices.sort()

    dices_diff = [dices[i+1]-dices[i] for i in range(N-1)]
    dices_diff.append(0)

    # print(dices)
    # print(dices_diff)

    target_ind = 0
    count = None
    total_dice = 0

    for i in range(N):
        # print("N: ", i)
        if dices_diff[i] != 0:
            if count == None:
                # print("count none")
                target_ind = i
                # print("target ind: ", target_ind)
            elif count<=0:
                # print("count: ". count)
                target_ind = i
                # print("target: ", target_ind)
            count = dices_diff[i]
            # print("new count: ", count)
        else:
            if count==None:
                pass
            else:
                # print("count reducing: ", count)
                count = count - 1

    

    # total_dice = N - target_ind
    if count == None and target_ind == 0:
        target_ind = N - 1
    # print("target ind", target_ind)

    total_dice = 0
    target_value = dices[target_ind]
    # print("target value", target_value)
    i = target_ind
    while i<N:
        # print("i", i)
        # print("target value", target_value)
        # print("dices", dices[i])
        if target_value > dices[-1]:
            # print("breaking")
            break
        if target_value<=dices[i]:
            # print("incrementing")
            total_dice = total_dice + 1
            target_value = target_value + 1
            # print("total dice", total_dice)
            # print("target_value:", target_value)
            
        else:
            break
        i = i + 1


    # print('total_dice', total_dice)
    target_value = dices[target_ind] - 1
    # print("target value", target_value)

    for i in range(target_ind-1, -1, -1):
        # print("i", i)
        if target_value<1:
            break
        if target_value <= dices[i]:
            # print("targe:", target_value)
            # print("dice", dices[i])
            total_dice = total_dice + 1
            target_value = target_value - 1
            
        else:
            break

    print("Case #" + str(t+1) + ": " + str(total_dice))
    # print(total_dice)




        
# 2 2 2 2 6 6 6 6 3 3 3 3 7 7 7 7 7 7 7 7