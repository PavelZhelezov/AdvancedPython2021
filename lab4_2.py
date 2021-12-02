def author(name):
	def wrapper(func):
		func._author=name
		return func
	return wrapper

@author("Dany Longo")
def add2(num:int) -> int:
	return num+2

print(add2._author)
