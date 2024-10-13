def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        res_ = i(int_list)
        results.update({i.__name__: res_})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))