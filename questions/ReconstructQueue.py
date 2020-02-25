class Solution:
	def reconstructQueue(self, people):
		people.sort(key=lambda x: (-x[0], x[1])) #O(n log(n)) the negative x[0] means tallest to smallest then x[1] means sort by k
		res = []
		for p in people: #O(n)
			res.insert(p[1], p) #O(n)
		return res
if __name__ == '__main__':
	print(Solution().reconstructQueue(
		[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))