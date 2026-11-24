# DZ1
# numbers = [8, 5, -3, 6, 64, 98, 22, -16]

# count_numb = len(numbers)
# for i in range(1, count_numb , 2):
#     print(numbers[i])

# DZ2
# numbers = [8, 5, -3, 6, 64, 98, 22, -16]

# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] % 2 == 0:
#         del numbers[i]

# print(numbers)

# # DZ3

# words = ["apple", "banana", "orange", "kiwi"]

# words.reverse()

# print(words)


# # DZ4

numbers = [8, 5, -3, 6, 64, 98, 22, -16]

average = sum(numbers) / len(numbers)

result = []

for num in numbers:
    if num < average:
        result.append(num)

print(result)