import random


def sumoProduct(l1, l2):
    if len(l1) != len(l2):
        raise ValueError('Both list must be equal in length')
    
    result = sum( x * y for x, y in zip(li, l2))
    return result    


numbers1 = [5, 3, 1, 1, 2]
numbers2 = [1, 2, 2, 9, 5]
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)


numbers1 = [random.randint(1, 10) for i in range(5)]
numbers2 = [random.randint(1, 10) for i in range(5)]
print('numbers 1 ', numbers1)
print('numbers 2 ', numbers2)
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)

##
