
def memoize(f):
	cache={}
	def memoized(*args):
		try:
			return cache[args]
		except KeyError:
			result = cache[args] = f(*args)
			return result
	return memoized


@memoize
def fibo(n):
	if n<2: return n
	else: return fibo(n-1)+fibo(n-2)

print fibo(200)