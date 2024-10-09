import circle
import square


figs = ['circle', 'square']  ''' All fugures '''
funcs = ['perimeter', 'area'] ''' All functions '''
sizes = {}

def calc(fig, func, size):
	'''fig: A string representing the figure type (either 'circle' or 'square').
	func: A string representing the function type (either 'perimeter' or 'area').
	size: A list of values representing the dimensions of the figure 
	(e.g., radius for a circle, side length for a square).'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')
	'''Response output'''

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
		'''The first loop prompts the user to enter a valid figure name. 
		It continues until the user provides a valid input found in the figs list.'''
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
		''' The second loop prompts the user to select a calculation function (perimeter or area) 
		from the funcs list, repeating until a valid input is received '''
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
		'''Size Input: The third loop requests the dimensions required for the calculation. 
		It checks the length of the size list against the expected number of parameters for the selected function-figure combination. 
		This is where the sizes dictionary is supposed to be used. 
		By default, it assumes at least one size (e.g., radius or side length).'''
	calc(fig, func, size)
	'''This is where the calculation takes place'''



