import collections
class Solution:
	def canConstruct(self, ransomNote, magazine):
		mag_dict = collections.defaultdict(int)
		for char in magazine:
			mag_dict[char] += 1
		for char in ransomNote:
			mag_dict[char] -= 1
			if mag_dict[char] < 0:
				return False
		return True

if __name__ == '__main__':
	print(Solution().canConstruct('aa', 'aab'))