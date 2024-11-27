import random
import string

def generate_passwords(names):
    password_dict = {}
    
    for name in names:
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_lowercase, k=4))
        password = numbers + letters
        password_dict[name] = password
    
    return password_dict

names = ['Bobur', 'Davron', 'Ilhom']
result = generate_passwords(names)
print(result)

def sum_of_divisors(n):
    divisors_sum = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum

number = 6
result = sum_of_divisors(number)
print(result)

def count_of_divisors(n):
    count = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    return count

number = 12
result = count_of_divisors(number)
print(result)
