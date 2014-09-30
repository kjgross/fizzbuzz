

def calculate_discount(item_cost, relative_discount, absolute_discount):
	""" Caluclate the sale price"""
	percent = float(relative_discount * 0.01)
	temp = item_cost - (item_cost * percent)

	if temp <= 0:
		raise ValueError("relative_discount too large")
	print temp

	final = temp - absolute_discount
	if final <= 0:
		raise ValueError("Overall Discount is too large")
	return final

def main():
	register_says = calculate_discount(100, 10, 30)
	print "This item costs ${:.2f}".format(register_says)

if __name__ == "__main__":
	main()
