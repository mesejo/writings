fruits = ['banana', 'apple', 'melon', 'guava', 'avocado']
demo = ['apple', 'avocado', 'banana']
ordering = {fruit: i for i, fruit in enumerate(fruits)}

res = sorted(demo, key=ordering.get)
print(res)  # ['banana', 'apple', 'avocado']
