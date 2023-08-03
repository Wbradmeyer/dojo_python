# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = 'Brad'
print('Hello', name + '!') # with a comma
print('Hello ' + name + '!') # with a +
# 3. print "Hello 42!" with the number in a variable
name = 40
print('Hello', str(name) + '!') # with a comma
print('Hello ' + str(name) + '!') # with a +
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = 'sushi'
fave_food2 = 'pizza'
print('I love to eat {} and {}.'.format(fave_food1, fave_food2)) # with .format()
print(f'I love to eat {fave_food1} and {fave_food2}.') # with an f string
food_one = 'gator tail'
food_two = 'french fries'
print('I love to eat {} and {}.'.format(food_one, food_two))
print(f'I love to eat {food_one} and {food_two}.')
print('I love to eat %s and %s.' % (food_one, food_two))

print(food_one.upper())
print(food_two.title())
print(food_two.count('f'))
print(food_one.endswith('s'))