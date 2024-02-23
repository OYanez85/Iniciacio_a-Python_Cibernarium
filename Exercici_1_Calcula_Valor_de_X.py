import statistics

x = [356.75, 487.45, 295.83, 532.00]

# Calculating the sum of the list x
total_sum = sum(x)
print('Total Sum in Euros:', total_sum)

# Calculating the median of the list x
median_value = statistics.median(x)
print('Median:', median_value)

y = (532 * 80) / 100
(print(y))

# Original list
x = [356.75, 487.45, 295.83, 532.00]

# Replacing the last value with 425.6
x[-1] = 425.6

print('Última comanda modificada', x)

# Calculating the sum of the list x
total_sum = sum(x)
print('Total Sum in Euros:', total_sum)
print(type(total_sum))

# Calculating the median of the list x
median_value = statistics.median(x)
print('Median:', median_value)
print(type(median_value))

# Calculating the sum of the list x
total_sum = sum(x)
print('Total Sum in Euros: ', str(total_sum))
print('Type of total_sum: ', str(type(total_sum)))

# Calculating the median of the list x
median_value = statistics.median(x)
print('Median: ', str(median_value))
print('Type of median_value: ', str(type(median_value)))