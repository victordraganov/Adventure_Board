from matrix import Matrix

class Battlefield(object):
	"""This class representes the place where all battles are processed.
		It's like a mini board where players fight."""

	INITIAL_HEIGHT = 7
	INITIAL_WIDTH = 10

	def __init__(self):
		self._fields = Matrix(INITIAL_HEIGHT, INITIAL_WIDTH) # Not for good

	# MUST GENERATE TALL AND SHORT OBSTACLES
	# MUST HAVE BACKGROUND (IN THE GUI)