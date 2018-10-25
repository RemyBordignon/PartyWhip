
class Date:

	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year

	def greaterThan(self, date):
		greater = False

		if (self.year > date.year) or (self.year == date.year and self.month > date.month) or (self.year == date.year and self.month == date.month and self.day > date.day):
			greater = True

		return greater