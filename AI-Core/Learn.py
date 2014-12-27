from __future__ import print_function
print ("1>Learn")
print ("2>Research")

comma = raw_input(">>>")

if comma == '1':
	enter = raw_input("Input:")
	enter_to = raw_input("to:")
	blank = ' '
	to_write_on_file = enter + blank + enter_to
	to_write_on_file_inverse = enter_to + blank + enter
	if enter in open('brain.txt').read():
		print("String already in file")

	else:
		brain = open('brain.txt', 'a')
		print(to_write_on_file, file=brain)
		print(to_write_on_file_inverse, file=brain)
		brain.close()
else:
	out = open('brain.txt', 'r')
	print (out.readlines())
	out.close()

	enter = raw_input("Term:")
	enter_second = raw_input("and:")
	full_enter = enter +' '+ enter_second

	if enter_second == '':
		string = True
	else:
		string = False

	if string == True:
		if enter in open('brain.txt').read():
			print("true")
		else:
			print("false")
	else:
		if full_enter in open('brain.txt').read():
			print("true")
		else:
			print("false")
