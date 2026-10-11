class Dungeon():
	def __init__(self):
		self.height = None
		self.width = None
		self.map = []
		
	def pull_dungeon(self):
		in_file = open("room_1.txt","r")
		for y in in_file:
			row = []
			for x in y.rstrip("\n"): # removes the new line char
				row.append(x)
			self.map.append(row)
		self.height = len(self.map)
		self.width = len(self.map[0])
		
		in_file.close()
		
	def draw_dungeon(self):
		for y in range(self.height):
			for x in range(self.width):
				print(self.map[y][x],end="")
			print()
