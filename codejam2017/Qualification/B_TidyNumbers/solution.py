T = int(input())
for i_case in range(1, T+1):
    N = input()
    digits = [int(c) for c in N]
    for i in range(1, len(digits)):
        if (digits[i] < digits[i-1]):
            j = i
            while (digits[j] < digits[j-1]) and (j > 0):
                digits[j-1] -= 1
                j -= 1
            for j in range(j+1, len(digits)):
                digits[j] = 9
    while digits[0] == 0:
        digits.pop(0)
    result = ''.join(str(d) for d in digits)
    print (f'Case #{i_case}: {result}')