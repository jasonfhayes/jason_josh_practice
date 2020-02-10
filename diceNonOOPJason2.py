import random
my_dict = {}
how_many = int(input('How many rolls? '))
for i in range(how_many):
	total = (random.randrange(1, 7)) + (random.randrange(1, 7))
	if total not in my_dict:
		my_dict[total] = 1
	else:
		temp_value = my_dict[total]
		temp_value = temp_value + 1
		my_dict[total] = temp_value
print('\nTotal:\tCount:\tPercetage:')
for i in range(2, 13):
	special_number = ('{:.2f}'.format((my_dict[i]/how_many)*100))
	print(f'{i}:\t{my_dict[i]}\t{special_number}%')
	
# hello world