# 1. Countdown
def countdown(num):
    new_list = []
    while num >= 0:
        new_list.append(num)
        num -= 1
    return new_list

print(countdown(5))


# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

# 3. First Plus Length
def first_plus_length(list):
    first_value = list[0]
    length = len(list)
    return (first_value + length)

print(first_plus_length([1,2,3,4,5]))


# 4. Values Greater than Second
def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    else:
        for x in list:
            if x > list[1]:
                new_list.append(x)
        print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# 5. This Length, That Value
def length_and_value(size, value):
    new_list = [value]
    return (new_list * size)

print(length_and_value(4,7))
print(length_and_value(6,2))