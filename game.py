from dungeon import Dungeon

class Game():

	@classmethod
	def start(cls):
		print("Welcome to Dungeon Crawl...")
		cls.main_loop()
	
	@classmethod	
	def main_loop(cls):
		Dungeon.pull_dungeon()
		Dungeon.draw_dungeon()
	
	@classmethod
	def update_game(cls):
		pass

	@classmethod	
	def game_over(cls):
		pass
