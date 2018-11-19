#!/usr/bin/env python

# title           : code_challenge.py
# description     : The given list can be partitioned into two sublists
# author          : jijin sebastian
# date            : 20181119
# python_version  : 2.7.15

#================================================================

class CodeChallenge:

	def __init__(self, num_list = []):
		self.num_list = num_list
		self.a = []
		self.b = []

	@staticmethod
	def get_sum(items=[]):
		"""
		To return total sum of the list
		"""

		result = 0
		if items:
			result = reduce(lambda x, y: x+y, items)
		return result

	def get_partitioned_list(self):
		"""
		Return two lists of equal sum
		"""

		
		for i in sorted(self.num_list, reverse=True):
			if self.get_sum(items=self.a) < self.get_sum(items=self.b):
				self.a.append(i)
			else:
				self.b.append(i)	
		
		print "This list can be partition"
		print "Input list :-", self.num_list
		print "Sum of the input list :-", self.get_sum(items=self.num_list)
		print "List One is :-", self.a
		print "Sum of the list one :-", self.get_sum(items=self.a)
		print "List Two is :-", self.b
		print "Sum of the list Two :-", self.get_sum(items=self.b)

	def check_partitionable(self):
		"""
		To check given list is partitioned or not.
		"""

		if self.get_sum(items=self.num_list) % 2 == 0:			
			self.get_partitioned_list()
		else:
			print "This list is not allow to partion by 2"

c1 = CodeChallenge(num_list=[1, 5, 2, 6, 4, 8])
c1.check_partitionable()