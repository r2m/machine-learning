from math import pow
class Point(object):

	def __init__(self, x, y):
		'''Defines x and y variables'''
		self.X = x
		self.Y = y

	def __str__(self):
		return "Point(%s,%s)"%(self.X, self.Y) 

	def distanceSquared(self, other):
		dx = pow(self.X - other.X, 2)
		dy = pow (self.Y - other.Y, 2)
		return dx + dy
