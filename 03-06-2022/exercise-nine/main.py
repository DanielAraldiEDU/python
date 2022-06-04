import numpy

array = numpy.zeros((3, 5))
print(array)

array = numpy.ones((3,5))
print(array)

array = numpy.array([10, 20, 30], dtype=numpy.float64)
print(array)

array = numpy.empty((2, 3))
print(array)

array = numpy.arange(5, 10, 0.5)
print(array)

array = numpy.linspace( 0, 2, 9 )
print(array)

array = numpy.random.random((2,3))
print(array)
