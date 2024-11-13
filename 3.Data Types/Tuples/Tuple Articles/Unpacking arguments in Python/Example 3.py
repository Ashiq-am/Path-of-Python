def arithmetic_operations(arr: list):
    MAX = max(arr)


    MIN = min(arr)
    SUM = sum(arr)
    AVG = SUM / len(arr)
    return (SUM, AVG, MAX, MIN)

if __name__ == '__main__':
    arr = [5, 8, 9, 12, 50, 3, 1]

    # for all data
    sum_arr, avg_arr, max_arr, min_arr = arithmetic_operations(arr)
    print("CASE 1 ", sum_arr, avg_arr, max_arr, min_arr)

    # for only avg and max
    _, avg_arr, max_arr, _ = arithmetic_operations(arr)
    print("CASE 2 ", avg_arr, max_arr)

    # for only sum and ming
    sum_arr, *_, min_arr = arithmetic_operations(arr)
    print("CASE 3 ", sum_arr, min_arr)
