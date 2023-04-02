import heapq


numbers = [0, 4, 6, 3, 2, 1, 9, 8, 7, 5]
largest = heapq.nlargest(3, numbers)
print(largest)  # [9, 8, 7]

fruits = ["apple", "banana", "tomato", "avocado", "mango",
          "pineapple", "coconut", "blueberry", "pear", "kiwi"]
smallest = heapq.nsmallest(3, fruits, key=len)
print(smallest)  # ['pear', 'kiwi', 'apple']
