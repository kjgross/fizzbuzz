import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
 	def testProperDiscountsApplied(self):
 		total = calculate_discount(100, 10, 30)
 		self.assertEqual(total, 60.00)

	def testZeroDiscount(self):
		total = calculate_discount(100, 0, 0)
		self.assertEqual(total, 100.00)	

	def testRelativeTooBig(self):
		with self.assertRaises(ValueError):
			total = calculate_discount(100,200,30)

	def testAbsoluteTooBig(self):
		with self.assertRaises(ValueError):
			total = calculate_discount(100,10,90)	




if __name__ == "__main__":
	unittest.main()