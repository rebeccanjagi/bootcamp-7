class StringSplosion(object):
	'''
	Write a function to output the folliwing
	 phone  => pphphophonphone
	 ab     => aab
	 like   => lliliklike

	'''

	def __init__(self , string):
		self.string = string

	def manipulate(self):
		result = ''
		for i in range(len(self.string)+1):
			result += self.string[:i]
		return result
