# # https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

# ! Expressions Matter --------------

def expression_matter(a, b, c):
    values = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c)
    ]

    return max(values)

    









# ! Grasshopper - Summation --------------

def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    return sum

    # return (1 + num) * num / 2








