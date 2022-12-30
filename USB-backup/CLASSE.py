class num():
	def __init__(self, n):
		self.n = n

	def bin(self):
		a = ''
		while self.n > 0:
			a += '0' if self.n%2 == 0 else '1'
			self.n = int(self.n/2)		
		return a[::-1]
		
s = num(int(input('n: ')))
print(s.bin())