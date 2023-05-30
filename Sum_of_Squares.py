def get_sqrd_val(x):
    return x*x
def get_sum_of_sqrs(list_a):
    sqrs_sum = 0
    for i in list_a:
        sqrs_sum += get_sqrd_val(i)
    return sqrs_sum
list_a = [1, 2, 3]
sum_of_sqrs = get_sum_of_sqrs(list_a)
print(sum_of_sqrs)