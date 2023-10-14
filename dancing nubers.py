dancing_limit = int(input())


def generate_dancing_numbers(dancing_limit):
    for i in range(dancing_limit + 1):
        if i < 10:
            yield i
            continue
        check = 1
        temp = i
        digit = temp % 10
        temp //= 10
        while temp > 0:
            if abs(digit - temp % 10) != 1:
                check = 0
                break
            digit = temp % 10
            temp //= 10
        if check:
            yield i


def print_dancing_numbers(dancing_limit):
    for dancing_number in generate_dancing_numbers(dancing_limit):
        print(dancing_number, end=" ")


print_dancing_numbers(dancing_limit)
