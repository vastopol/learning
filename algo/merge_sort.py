
def mergesort(A):
	if len(A) <= 2:
		return A
	else:
		m = len(A)/2
		l = mergesort(A[:m])
		r = mergesort(A[m:])
		return merge(l,r)

def merge(l,r):
	result, i, j = [], 0, 0
	while i < len(l) and j < len(r):
		if l[i] <= r[j]:
			result.append(l[i])
			i += 1
		else:
			result.append(r[j])
			j += 1
	result += l[i:]
	result += r[j:]
	return result

