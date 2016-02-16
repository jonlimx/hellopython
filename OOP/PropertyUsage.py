# In this demo, we use python property to force budget to be passive.
# If you try to assign a negative value, you will get a exception thrown.

class Movie(object):
	def __init__(self, title, rating, runtime, budget, gross):
		self._budget = None
		self.title = title
		self.runtime = runtime
		self.gross = gross
		self.budget = budget

	@property
	def budget(self):
		return self._budget

	@budget.setter
	def budget(self, value):
		if value < 0:
			raise ValueError("Negative value not allowed: %s" % value)
		self._budget = value

	def profit(self):
		return self.gross - self.budget

if __name__ == '__main__':
	m = Movie('Casablanca', 97, 102, 964000, 1300000)
	print m.budget
	try:
		m.budget = -100
	except ValueError,e:
		print e
