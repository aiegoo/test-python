a = {'apple', 'lemon', 'banana'}
a.update(('kiwi', 'banana'))
a.remove('lemon')
a.add('apple')
for i in a:
      print("Fruit name : %s" % i)
# output
# Fruit name : banana
# Fruit name : apple
# Fruit name : kiwi
