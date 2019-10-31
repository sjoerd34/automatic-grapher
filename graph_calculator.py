filename = 'data7.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

mv_values = ''
for line in lines:
	if line == ('\n'):
		mv_values += line.rstrip()
	else:
		mv_values += line.rstrip('\n') + ' '


mv_values = mv_values.replace(',', '.')
mv_list = mv_values.split(' ')
mv_list.pop()

mv_list = list(map(float, mv_list))
stap = 10
schaal_verdeling = list(range(0,140,stap))
counter = 0
for i in mv_list:
	counter += 1
	for b in schaal_verdeling:
		if i < (b + stap):
			print('#' + str(counter) + ' ' + str(b) + ' en ' + str(round(((i / 1)%stap),2)) + ' vakjes\n')
			break


