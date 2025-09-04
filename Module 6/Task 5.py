def number(list):
    new_list = []
    for num in list:
        if num % 2 != 0:
            new_list.append(num)
    return new_list

my_list = [1,2,3,4,5]
x= number(my_list)
print(my_list)
print(x)
