cities = ['Seoul', 'Keyonggi', 'Inchoen', 'DAejeon', 'Daegu', 'Ulsan', 'Busan'];
str01 = 'S'
print(cities)
print(cities[0], cities[-1])
print(cities[1:4])
print(cities[2:])
for i in cities:
    str01 = str01 + i[1]
print(str01)

# Output:
# ['Seoul', 'Keyonggi', 'Inchoen', 'DAejeon', 'Daegu', 'Ulsan', 'Busan']
# Seoul Busan
# ['Keyonggi', 'Inchoen', 'DAejeon']
# ['Inchoen', 'DAejeon', 'Daegu', 'Ulsan', 'Busan']
# SeoulKeyInDAeDaUlsBus

# ['Seoul', 'Keyonggi', 'Inchoen', 'DAejeon', 'Daegu', 'Ulsan', 'Busan']
# Seoul Busan
# ['Keyonggi', 'Inchoen', 'DAejeon']
# ['Inchoen', 'DAejeon', 'Daegu', 'Ulsan', 'Busan']
# SeenAalu
