def frequency_check(check_list1, check_list2):
    tempList = []

    for i in range(len(check_list1)):
        tempList.append(check_list1[i] * check_list1[i])

    if len(check_list1) == len(check_list2) and tempList == check_list2:

        print("Two lists are matched")

    else:

        print("Two lists are unmatched")


frequency_check([1, 2, 3, 2, 5, 6], [1, 4, 9, 4, 25, 36])
