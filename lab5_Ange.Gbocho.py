"""
Original version
def minimum(some_list):
    a = 0
    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
    return a
numbers = [5, 12, 3, 8]
print(minimum(numbers))
"""
# Corrected version
def minimum(some_list):
    a = some_list[0]

    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]

    return a

numbers = [5, 12, 3, 8]
print(minimum(numbers))
