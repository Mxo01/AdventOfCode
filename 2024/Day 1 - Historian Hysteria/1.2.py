list1 = []
list2 = []
similarity_score = 0

f = open('puzzle.txt', 'r')

for line in f:
	location_id_1 = int(line.split('   ')[0])
	location_id_2 = int(line.split('   ')[1])
	list1.append(location_id_1)
	list2.append(location_id_2)

for pos in range(len(list1)):
	location_id_1 = list1[pos]
	location_id_1_count_in_list2 = list2.count(location_id_1)

	similarity_score += location_id_1 * location_id_1_count_in_list2

f.close()

print(similarity_score)