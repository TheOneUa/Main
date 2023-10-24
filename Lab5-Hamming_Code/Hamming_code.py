input_string = "000111000111000111000000000111111000111000000000000111111000000111000111000000111000000000000000000111000111000000111111000111111000000111000111000111111000111111111000000111111111000000111111000111111000000111000111000111111000111000000111000000111000000000000000000111111111000111000000000111111000111111111111000111111000111111000000000111111000000111000000000000111000000000000000000111111000111111000111000111111000000111000111000000111000000000000000000111111111000111000000000111111000111000000000000111111000000000000111000111111111000111000000000000111000000000000000000111111000111000000111000000111000000000000000000111111000000000111111000111111000000000000111000111111000111111111000000000111000000000000000000111111000000111000000000111111000111111111111000000111000000000000000000111111111000111000000000111111000111000000000000111111000111000000111000111111111000000111111000000111000000000000000000111111000111000111111000111111000000000000111000111111111000111000000000111111000000000000111"

# ділимо строку по 24 символи
subgroups = [input_string[i:i+24] for i in range(0, len(input_string), 24)]

# переводимо коджну підгруппу в двійковий код
binary_result = []

for subgroup in subgroups:
    elements = [subgroup[i:i+3] for i in range(0, len(subgroup), 3)]
    binary_string = ""

    for element in elements:
        count_0 = element.count('0')
        count_1 = element.count('1')

        if count_0 > count_1:
            binary_string += '0'
        else:
            binary_string += '1'

    binary_result.append(binary_string)

# обьеднуємо підгруппи
binary_data = ''.join(binary_result)

# переводимо в ASCII
ascii_result = ""
for i in range(0, len(binary_data), 8):
    ascii_char = chr(int(binary_data[i:i+8], 2))
    ascii_result += ascii_char

# результат
print("початкова строка:", input_string)
print("В двійковому коді:", binary_data)
print("Результат в ASCII:", ascii_result)
