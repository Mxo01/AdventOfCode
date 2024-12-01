list1 = []
list2 = []
total_distance = 0

f = open('puzzle.txt', 'r')

for line in f:
	location_id_1 = int(line.split('   ')[0])
	location_id_2 = int(line.split('   ')[1])
	list1.append(location_id_1)
	list2.append(location_id_2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

for pos in range(len(sorted_list1)):
	location_id_list1 = sorted_list1[pos]
	location_id_list2 = sorted_list2[pos]

	distance = abs(location_id_list1 - location_id_list2)

	total_distance += distance

f.close()

print(total_distance)