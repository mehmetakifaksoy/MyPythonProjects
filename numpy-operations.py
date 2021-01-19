import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,40,6)


print(numbers1)
print(numbers2)


result = numbers1 + numbers2
result = numbers1 - numbers2
result = numbers1 * numbers2
result = numbers1 / numbers2
result = numbers1 * 10
result = np.sin(numbers2)
result = np.tan(numbers2)
result = np.log(numbers2)


print(result)