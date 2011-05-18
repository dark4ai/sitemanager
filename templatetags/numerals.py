from django.template import Library, Node, TemplateSyntaxError
from django.utils.encoding import iri_to_uri

register = Library()
        
def num_func(n, arr):
	if n % 10 == 1 and n % 100 != 11:
		return arr[0]
	elif n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
		return arr[1]
	return arr[2]	
		
def numerals(n, arr, hide_num=False):
	try:
		n = int(n)
		if len(arr) != 3:
			raise TypeError()
	except ValueError:
		raise TemplateSyntaxError("first argument of 'numerals' tag must be integer, but = '%s'." % parser.compile_filter(args[1]))
	except TypeError:
		raise TemplateSyntaxError("second argument of 'numerals' tag must be array of 3 items")
	result = num_func(n, arr)
	if hide_num:
		return result
	return "%d %s" % (n, result)

numerals = register.simple_tag(numerals)
