class Person:
    department = 'School of information'

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


store1 = [1, 2, 3, 4, 5]
store2 = [1, 2, 3, 4, 5]

cheapest = map(min, store1, store2)

# Lambda
my_function = lambda a, b, c: a + b

my_function(1, 2, 3)

# my_list = []
# for number in range(0, 100):
#     if number % 2 == 0:
#         my_list.append(number)

my_list = [number for number in range(0, 100) if number % 2 == 0]

print(my_list)



lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids





















