class GeometricShape:
	def __init__(self,size):
		self.size = size
		self.constructShape()

	def constructShape(self):
		numbers = list(range(1,self.size+1))
		connections = {}
		size = self.size
		diagonals = self.getDiagonals(size)
		for i in range(size):
			numbers.pop()
			connections[number] = None




	@staticmethod
	def getDiagonals(n):
		return (n - 3) 









		"""
		Example Shape Format
		[1,3]
		[3,5]
		[5,1]

		  1
		   
		5   3
		
		[]
		[]
		[]
		[]
		*     *

           *  
      
		*     *
		
		[]
		[]
		[]
		[]
		[]
		[]

		  *  *
		*      *

		*      *
		  *  *

		"""
