# Debugger in Python
'''
import pdb

def calculate_average(numbers):
    pdb.set_trace()

    total = sum(numbers)
    avg = total/len(numbers)
    return avg

numbers_list = []
print(calculate_average(numbers_list))
'''

# Unit Testing in python
'''
import unittest
# Function to test
def add(a,b):
    return a + b

# Unit test class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(0,0), 3)

# Run tests
unittest.main(argv=[''], exit=False)

print("Thank you")
'''

# Integration Testing

class Database:
    def __init__ (self):
        self.users = {}

    def add_user(self, user_id, name):
        if user_id in self.users:
            print("USer already exists!")
            raise ValueError("User exists")
        self.users[user_id] = name
        print("User added successfully!")

    def get_user(self, user_id):
        return self.users[user_id]
