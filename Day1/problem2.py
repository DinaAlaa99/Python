
def removeSimilarNumbers(old_list):
    new_list = list(dict.fromkeys(old_list))
    return new_list


old_list = [1, 2, 2, 2, 3, 4]
new_list = removeSimilarNumbers(old_list)
print(new_list)

