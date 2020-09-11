import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# duplicates = [ name for name in names_1 if name in names_2 ]  # Return the list of duplicates in this data structure // 1.60 second runtime
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1) #// 8.96 second runtime

'''class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()
# create a new stack
search = Stack()
# for every name in our first array, add that to our stack
for name in names_1:
    search.push(name)

# for each item on our stack, if it's in our second array append it to our duplicates
for item in search.storage:
    if item in names_2:
        duplicates.append(item) 
# 1.57 second runtime'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
