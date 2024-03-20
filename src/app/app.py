import customtkinter as tk
import asyncio
import asyncpg

from dotenv import load_dotenv
import os 

load_dotenv()

class App:
	async def exec(self):
		self.window = Window(asyncio.get_event_loop())
		await self.window.show()

class Window(tk.CTk):
	def __init__(self, loop):
		self.loop = loop 
		super().__init__()
		self.geometry("800x500")

	# sets up database
	async def setup(self):
		try:
			self.conn = await asyncpg.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), port=os.getenv("DB_PORT"), password=os.getenv("DB_PASSWORD"), database="studentsystem")
		# if the database does not exist, it will reconnect to the default template1 database
		except asyncpg.InvalidCatalogNameError:
			self.conn = await asyncpg.connect( host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), port=os.getenv("DB_PORT"), password=os.getenv("DB_PASSWORD"), database="template1")
			# creates database studentsystem 
			await self.conn.execute(f"CREATE DATABASE studentsystem OWNER {os.getenv('DB_USER')}")
			await self.conn.close()
			self.conn = await asyncpg.connect( host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), port=os.getenv("DB_PORT"), password=os.getenv("DB_PASSWORD"), database="studentsystem")
		await self.conn.execute("CREATE SCHEMA IF NOT EXISTS main")

	async def show(self):
		await self.setup()
		while True:
			self.update()
			await asyncio.sleep(0.1)

	async def default_widgets(self):
		# TODO: default labels and more
	
	async def selections(self):
		# TODO: selction frame at first run
		pass 

	async def search_bar(self):
		# TODO: mutable search entry

