def next_palindrome(digit_list):
    c[7] += 1
    n = len(digit_list)
    mid = n // 2
    if n % 2 == 0:
        c[1] += 1
        left_side = digit_list[:mid]
        left_side_reverse = left_side[::-1]
        candidate = left_side + left_side_reverse
    else:
        c[2] += 1
        #Bug: Replace with
        left_side = digit_list[:mid]
        middle = digit_list[mid]
        left_side_reverse = left_side[::-1]
        candidate = left_side + [middle] + left_side_reverse
    if candidate > digit_list:
        c[3] += 1
        return candidate
    for i in range(mid - 1, -1, -1):
        c[4] += 1
        if digit_list[i] < 9:
            c[5] += 1
            digit_list[i] += 1
            if i != n - i - 1:
                c[6] += 1
                digit_list[n - i - 1] = digit_list[i]
            return digit_list[:mid] + [digit_list[mid]] * (n % 2) + digit_list[mid - 1::-1]
        digit_list[i] = 0
        digit_list[n - i - 1] = 0
    return [1] + [0] * (n - 1) + [1]
