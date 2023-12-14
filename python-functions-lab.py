# Exercise 1

def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(sum_to(6))
print(sum_to(10))

# Exercise 2

def largest(list):
    return max(list)

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

# Exercise 3

def occurrences(string, substring):
    return string.count(substring)

print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))

# Exercise 4

def product(*args):
    ans = 1
    for arg in args:
        ans *= arg
    return ans

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))

# Bonus

def steps_to_zero(int):
    steps = 0
    while int > 0:
        if int % 2 == 0:
            int /= 2
            steps += 1
        else:
            int -= 1
            steps += 1
    return steps

print(steps_to_zero(14))