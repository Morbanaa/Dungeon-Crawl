from dungeon import Dungeon

class Game():
	def __init__(self):
		self.dungeon = Dungeon()

	def start(self):
		print("Welcome to Dungeon Crawl...")
		self.main_loop()
		
	def main_loop(self):
		self.dungeon.pull_dungeon()
		self.dungeon.draw_dungeon()
		
	def process_input(self):
		pass
		
	def update_game(self):
		pass
		
	def game_over(self):
		pass
