immutable_var = 1, 2, 3,  True, "Hi Ganger"
print('immutable_var:', immutable_var)

#immutable_var[0] = 2  #Нельзя изменить элемент кортежа. Т.к. он не изменяем. Но можно изменить элемент списка находящийся в кортеже.
#print(immutable_var)

mutable_list = [1, 2, 2.2, 1], 'Welcome Ganger'
mutable_list[0][0] = 4
print('mutable_list:', mutable_list)
