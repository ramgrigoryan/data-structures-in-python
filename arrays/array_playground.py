numbers = [1,2,3,4,5]


#Add to the end
numbers.append(6)

numbers.append(7)

#Insert at position
numbers.insert(1,1)


#Remove last el
numbers.pop()

#Remove el on index
numbers.pop(0)

#Remove first appearance
numbers.remove(1)


new_numbers = numbers.copy()

new_numbers.pop()

print(new_numbers==numbers)

print(numbers)