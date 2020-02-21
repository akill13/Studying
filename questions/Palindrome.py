class Solution:
	def longestPalindrome(self, s: str) -> str:
		def expandPalindrome(s, start, end):
			res = [start, end]
			while start >= 0 and end < len(s) and s[start]==s[end]:
				res = [start, end]
				start-=1
				end+=1
			return res
		output = ""
		for i in range(len(s)):
			start, end = expandPalindrome(s, i, i)
			if end - start + 1 > len(output):
				output = s[start:end+1]
		for j in range(len(s)-1):
			if s[j] != s[j+1]:
				continue
			start, end = expandPalindrome(s, j, j+1)
			if end - start + 1 > len(output):
				output = s[start:end+1]
		return output

def main():
	s = input()
	s = s.strip()
	print(Solution().longestPalindrome(s))

if __name__ == '__main__':
    main()