def merge_sorted_arrays(arr1,arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    merged_array = []
    ar_copy_1 = arr1.copy()
    ar_copy_1.reverse()
    ar_copy_2 = arr2.copy()
    ar_copy_2.reverse()

    for i in range(len(ar_copy_1)-1,-1,-1):
        num1 = ar_copy_1[i]
        for j in range(len(ar_copy_2)-1,-1,-1):
            num2 = ar_copy_2[j]
            if num1<=num2:
                merged_array.append(ar_copy_1.pop())
                break
            else:
                merged_array.append(ar_copy_2.pop())
    print("end result",ar_copy_1,ar_copy_2)
    if len(ar_copy_1) ==0:
        for i in ar_copy_2:
            merged_array.append(ar_copy_2.pop())
    if len(ar_copy_2)==0:
        for i in ar_copy_1:
            merged_array.append(ar_copy_1.pop())
    print(merged_array)
    return merged_array

merge_sorted_arrays([0,2,4,7,7,7,9,11],[-5,2,5,7,8,10,12])


