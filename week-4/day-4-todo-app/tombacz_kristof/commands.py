import store
import datetime

def lists(list):
	if list != []:
		i = 1
		print('')
		for n in list:
			print(i, n['description'], n['status'], n['due date'])
			i += 1
		print('')
	else:
		print('\n' + '\033[31m' + 'The to-do list is empty!\n')

def add(list):
	user_input = input('\033[47m' + '\nPlease enter a new items to your to-do list: ')
	user_input_date = input('Enter the due date in the format(2015.12.03): ')
	list.append({'description': user_input, 'status': 'TO DO', 'due date': user_input_date})
	store.save(list)

def complete(list):
	user_input = input('\nPlease enter the number to complete: ')
	print('')
	n = int(user_input) - 1

	list[n]['status'] = 'DONE'

	store.save(list)

def removes(list):
	user_input = input('\nPlease enter the number to remove: ')
	print('')
	n = int(user_input) - 1

	list.pop(n)

	store.save(list)

def remove_completed(list):
	for n in list:
		if n['status'] == 'DONE':
			list.remove(n)
	for n in list:
		if n['status'] == 'DONE':
			list.remove(n)

	print('\nAll DONE items deleted!\n')
	store.save(list)
