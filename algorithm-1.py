def minSwaps(row):
    swaps = 0
    for i in range(0, len(row), 2):                     # Iterating through the loop once
        couple = (row[i] // 2, row[i + 1] // 2)         # Check for if the couples match
        if couple[0] != couple[1]:                      # If not  
            for j in range(i + 2, len(row)):            # continue iteration through the rest of the loop, checking each element for its match
                if row[j] //2 == couple[0]:
                    temp = row[i + 1]
                    row[i + 1] = row[j]
                    row[j] = temp
                    swaps += 1
                    break

    return swaps

# Test cases
print(f'case 1: {minSwaps([0, 1, 2, 3])}')
print(f'case 2: {minSwaps([3, 2, 0, 1])}')
print(f'case 3: {minSwaps([0, 2, 1, 3])}')
print(f'case 4: {minSwaps([2, 5, 3, 1, 4, 6])}')