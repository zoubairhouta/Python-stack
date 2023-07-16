def selection(arr):
    print(arr)
    count = 0

    while count < len(arr):
        min_index = count

        for i in range(count + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        arr[count], arr[min_index] = arr[min_index], arr[count]
        count += 1

    print(arr)