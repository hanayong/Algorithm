def mergeSort(a_list):
    # print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        print("[lefthalf]", lefthalf)
        print("[righthalf]", righthalf)

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k] = lefthalf[i]
                i = i + 1
            else:
                a_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    # print("Merging ", a_list)


alist = [6, 2, 4, 1, 3, 7, 5, 8]
mergeSort(alist)
print(alist)
