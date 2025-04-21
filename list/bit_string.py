def count_ways(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == "0" and bits[j] == "1":
                result += 1
    return result


bit_string = ["0", "1", "0", "0", "1", "0", "1", "1"]
print(count_ways(bit_string))
