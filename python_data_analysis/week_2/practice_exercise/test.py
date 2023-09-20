def dict_copies(my_dict, num_copies):
    answer = []
    for i in range(num_copies):
        answer.append(dict(my_dict))
    return answer

test_dict = dict_copies({'a':1, 'b':2}, 2)
test_dict[1]["a"] = 3
#my_diction, num_copies_t = {}, 2
#print(dict_copies(my_diction, num_copies_t))
print(test_dict)
