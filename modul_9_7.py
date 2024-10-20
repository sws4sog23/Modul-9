# def sum_three(a, b, c):
#     sum_ = a + b + c
#     return sum_


def is_prime(func):
    def wrapper(*args, **kwargs):
        res_ = func(*args, **kwargs)
        if res_ == 1:
            print('Ни простое, ни составное')
        elif res_ == 2:
            print('Простое')
        else:
            flg_ = True
            for i in range(2, res_):
                if res_ % i == False:
                    flg_ = False
                    break
            if flg_ == True:
                print('Простое')
            else:
                print('Составное')
        return res_

    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

# sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)
