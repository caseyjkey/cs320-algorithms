import sys

# provided
def read_array(filename):
    in_list = []
    with open(filename, 'r+') as input_file:
        for line in input_file:
            in_list.append(int(line))
    return in_list

def sort(in_list):
	if len(in_list) == 1:
		return in_list, 0
	middle = len(in_list) // 2
	left, lc = sort(in_list[:middle])
	right, rc = sort(in_list[middle:])
	merge, mc = merge_i(left, right, in_list)
	return merge, lc + rc + mc
	
# implement
def count_inversions(in_list):
	result = sort(in_list)
	return result[1]

# implement
def merge_i(l_list, r_list, in_list):
	result, count = [], 0
	indexLeft, indexRight = 0, 0
	lenLeft, lenRight = len(l_list), len(r_list)
	while indexLeft < lenLeft and indexRight < lenRight:
		if l_list[indexLeft] <= r_list[indexRight]:
			result.append(l_list[indexLeft])
			indexLeft += 1
		else:
			result.append(r_list[indexRight])
			indexRight += 1
			count += lenLeft - indexLeft
	result.extend(l_list[indexLeft:])
	result.extend(r_list[indexRight:])
	return result, count

# provided
if __name__ == '__main__':
    filename = sys.argv[1]
    in_list = read_array(filename)
    print(count_inversions(in_list))
