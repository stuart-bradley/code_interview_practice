# Cracking the coding interview - C7 - Object-Oriented Design
# Stuart Bradley
# 10-08-2016

import random
import collections
import time
import math

# Design a deck of cards and subclass a blackjack game. 
class Ex_1_Deck_Of_Cards:
	card_numbers = ["Ace","2","3","4","5","6","7","8","9","10", "Jack", "Queen", "King"]
	suits = ["Spade", "Club", "Diamond","Heart"]

	def __init__(self):
		self.deck = []
		for suit in Ex_1_Deck_Of_Cards.suits:
			for num in Ex_1_Deck_Of_Cards.card_numbers:
				card = Card(suit, num)
				self.deck.append(card)

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		if len(self.deck) > 0:
			return self.deck.pop()
		else:
			return None
class Card:
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

class BlackJack(Ex_1_Deck_Of_Cards):
	def __init__(self, players = 1):
		super(BlackJack, self).__init__()

		self.shuffle()

		dealer_cards = []
		dealer_cards.append(self.draw())
		dealer_cards.append(self.draw())

		self.dealer = Player("Dealer", dealer_cards)

		self.players = []
		for i in range(players):
			cards = []
			cards.append(self.draw())
			cards.append(self.draw())
			self.players.append(Player("Player " + str(i), cards))

	# Dealer always wins as there is no player input (always draw).
	def play_game(self):
		bust_players = []
		while len(bust_players) < len(self.players):
			dealer_value = self.get_blackjack_value(self.dealer.cards)
			if dealer_value == 21:
				return "Dealer wins."
			for player in self.players:
				if player not in bust_players:
					player.cards.append(self.draw())
					player_value = self.get_blackjack_value(player.cards)
					if player_value > 21:
						bust_players.append(player)
		return "Dealer wins."


	def get_blackjack_value(self, cards):
		values = [0]
		for card in cards:
			if card.number == "Ace":
				tmp_values = []
				for i in range(len(values)):
					tmp_values.append(values[i] + 11)
					values[i] += 1
				values.extend(tmp_values)
			elif card.number in ["Jack", "Queen","King"]:
				for i in range(len(values)):
					values[i] += 10
			else:
				for i in range(len(values)):
					values[i] += int(card.number)

		return min(values)

class Player:
	def __init__(self, name, cards=[]):
		self.name = name
		self.cards = cards

# Build a call centre with multiple respondant levels. 
class Ex2_Call_Centre:
	def __init__(self):
		self.respondants = [Respondant()]
		self.managers = [Manager()]
		self.directors = [Director()]

	def dispatch_call(self, call):
		for respondant in self.respondants:
			if respondant.call == None:
				respondant.call = call
				return True
		for manager in self.managers:
			if manager.call == None:
				manager.call = call
				return True
		for director in self.directors:
			if director.call == None:
				director.call = call
				return True
		return False

class Employee:
	def __init__(self):
		self.call = None

class Respondant(Employee):
	def __init__(self):
		super(Respondant, self).__init__()

class Manager(Employee):
	def __init__(self):
		super(Manager, self).__init__()

class Director(Employee):
	def __init__(self):
		super(Director, self).__init__()

class Call:
	def __init__(self):
		pass

# Jukebox
class Ex3_Jukebox:
	def __init__(self):
		self.songs = {}
		self.songs["Get Low - Lil Jon & The East Side Boyz"] = Song("Get Low - Lil Jon & The East Side Boyz")

		self.song_queue = collections.deque()

	def add_song(self, song_name):
		self.song_queue.append(self.songs[song_name])

	def now_playing(self):
		return self.song_queue[-1].name

class Song:
	def __init__(self, name):
		self.name = name

# Parking Lot
class Ex4_Parking_Lot:
	def __init__(self, spaces = 2):
		self.spaces = []
		for i in range(spaces):
			self.spaces.append(Space())
		self.cost_per_time_unit = 100

	def enter_space(self, car):
		for space in self.spaces:
			if not space.filled:
				space.filled = True 
				space.filled_start_time = time.time()
				time.sleep(0.001)
				car.space = space
				return True
		return False

	def exit_space(self, car): 
		space = car.space
		space.filled = False 
		start_time = space.filled_start_time
		space.filled_start_time = 0.0

		return (time.time() - start_time) * self.cost_per_time_unit


class Space:
	def __init__(self):
		self.filled = False
		self.filled_start_time = 0.0

class Car:
	def __init__(self):
		self.space = None

# Online book reader.
class Ex5_Library:
	def __init__(self):
		self.books = {}
		self.books["A Book"] = Book("A Book", "For sale: Baby shoes. Never worn.")

	def get_book(self, book_title):
		return self.books[book_title]

class Book:
	def __init__(self, name, text):
		self.name = name
		self.text = text

# Jigsaw puzzle solver.
class Ex6_Jigsaw:
	def __init__(self, pieces):
		self.board_size = int(math.sqrt(len(pieces)))
		self.board = [[0 for x in range(self.board_size)] for y in range(self.board_size)] 
		self.edges = []
		self.corners = []
		self.internal_pieces = []
		self.pieces_left = len(pieces)
		self.corner_positions = [(0,0),(0,self.board_size-1),(self.board_size-1,0),(self.board_size-1,-1)]

		for piece in pieces:
			piece.check_edge_and_corner()
			if piece.edge and not piece.corner:
				self.edges.append(piece)
			elif piece.corner:
				self.corners.append(piece)
			else:
				self.internal_pieces.append(piece)

	def solve_jigsaw(self):
		for piece in self.corners:
			if piece.up == None:
				if piece.left == None:
					self.board[0][0] = piece
					self.pieces_left -= 1
				elif piece.right == None:
					self.board[0][-1] = piece
					self.pieces_left -= 1
			elif piece.down == None:
				if piece.left == None:
					self.board[-1][0] = piece
					self.pieces_left -= 1
				elif piece.right == None:
					self.board[-1][-1] = piece
					self.pieces_left -= 1

		if self.pieces_left == 0:
			return True

		edge_positions = []
		internal_positions = []
		for x in range(0,self.board_size):
			for y in range(0,self.board_size):
				if x == 0 or x == self.board_size - 1 and (x,y) not in self.corner_positions:
					edge_positions.append((x,y))
				elif y == 0 or y == self.board_size - 1: 
					edge_positions.append((x,y))
				elif (x,y) not in self.corner_positions:
					internal_positions.append((x,y))

		for x,y in edge_positions:
			for piece in self.edges:
				if Piece.fits_with(self.board[x][y], piece):
					self.board[x][y] = piece
					self.pieces_left -= 1
					break

		for x,y in internal_positions:
			for piece in self.internal_pieces:
				if Piece.fits_with(self.board[x][y], piece):
					self.board[x][y] = piece
					self.pieces_left -= 1
					break

		if self.pieces_left == 0:
			return True
		else:
			return False


class Piece:
	def __init__(self, up=None, down=None, left=None, right=None, name=None):
		self.up = up
		self.down = down
		self.left = left
		self.right = right
		self.name = name

		self.edge = False
		self.corner = False

	def check_edge_and_corner(self):
		if None in [self.up, self.down, self.left, self.right]:
			self.edge = True

		if [self.up, self.down, self.left, self.right].count(None) > 1:
			self.corner = True

	
	@classmethod
	def fits_with(cls, piece_1, piece_2):
		if piece_2 in piece_1.__dict__.values():
			return True
		else:
			return False

# Chat server.
class Ex7_Chat_Server:
	def __init__(self, users={}):
		self.users = users

	def add_user(self, user):
		self.users[user.name] = user
		user.chat_server = self

	def relay_message(self, message):
		reciever = self.users[message.to.name]
		reciever.recieve_message(message)

class User:
	def __init__(self, name):
		self.name = name
		self.message_queue = collections.deque()
		self.chat_server = None

	def send_message(self, text, to):
		message = Message(text, self, to)
		self.chat_server.relay_message(message)

	def recieve_message(self, message):
		self.message_queue.append(message.text)

	def get_latest_message(self):
		self.message_queue.popleft()

class Message:
	def __init__(self, text, sender, to):
		self.text = text
		self.sender = sender
		self.to = to 

# Reversi
class Ex8_Reversi_Board:
	def __init__(self):
		self.board = [[None for x in range(8)] for y in range(8)] 
		self.players = [Player_Reversi("Black"), Player_Reversi("White")]
		self.played_disks = []

	def play_game(self, moves = []):
		for i,move in enumerate(moves):
			x,y = move
			player = self.players[i % 2]
			if self.board[x][y] == None:
				disk = Disk(player.colour, (x,y))
				self.board[x][y] = disk
				self.played_disks.append(disk)
			self.check_disks()
		if self.players[0].points > self.players[1].points:
			return "Black wins!"
		elif self.players[0].points < self.players[1].points:
			return "White wins!"
		else:
			return "Draw!"

	def check_disks(self):
		for disk in self.played_disks:
			if disk.check_and_update(self.board):
				if disk.colour == "Black":
					self.players[0].points += 1
				else:
					self.players[1].points += 1

class Disk:
	def __init__(self, colour, position):
		self.colour = colour
		self.position = position

	def check_and_update(self, board):
		x,y = self.position 
		neighbours = [((x+1,y),(x-1,y)),((x,y+1),(x,y-1))]
		for neigh_1, neigh_2 in neighbours:
			x_1, y_1 = neigh_1
			x_2, y_2 = neigh_2
			if 0 <= x_1 < len(board) and 0 <= y_1 < len(board) and 0 <= x_2 < len(board) and 0 <= y_2 < len(board):
				if board[x_1][y_1] != None and board[x_2][y_2] != None:
					if board[x_1][y_1].colour == board[x_2][y_2].colour and board[x_1][y_1].colour != self.colour:
						if self.colour == "Black":
							self.colour = "White"
						else:
							self.colour = "Black"
						return True
		return False

	def __str__(self):
		return self.colour

class Player_Reversi:
	def __init__(self, colour):
		self.colour = colour
		self.points = 0

# Circular Array
class Ex9_Circular_Array:
	def __init__(self, nodes):
		self.first_node = nodes[0]
		for i in range(1,len(nodes)):
			nodes[i-1].next_node = nodes[i]

			if i == len(nodes) - 1:
				nodes[i].next_node = nodes[0]

	def rotate(self):
		self.first_node = self.first_node.next_node

	def iterator(self):
		node = self.first_node
		yield node
		node = node.next_node
		while node != self.first_node:
			yield node
			node = node.next_node

class Circular_Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node

# Minesweeper
class Ex10_Minesweeper:
	def __init__(self, size, bombs):
		self.board = [[Cell() for x in range(size)] for y in range(size)] 
		self.bomb_cells = []


		#bomb_positions = random.sample(range(size*size), bombs)
		bomb_positions = [0,1]
		random_counter = 0
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				current_cell = self.board[x][y]
				if 0 <= x - 1 < size:
					self.board[x-1][y].neighbours.append(current_cell)
					current_cell.neighbours.append(self.board[x-1][y])
				if 0 <= y - 1 < size:
					self.board[x][y-1].neighbours.append(current_cell)
					current_cell.neighbours.append(self.board[x][y-1])

				# Make bomb if in sample.
				if random_counter in bomb_positions:
					current_cell.bomb = True
					self.bomb_cells.append(current_cell)
				random_counter += 1

		# Create counters.
		for bomb_cell in self.bomb_cells:
			for neighbour in bomb_cell.neighbours:
				neighbour.count += 1

	def play_game(self, moves=[]):
		for x,y in moves:
			if self.board[x][y].bomb: 
				self.board[x][y].visible = True
				return "Loser!"
			elif self.board[x][y].count > 0:
				self.board[x][y].visible = True
			else:
				calculate_view(x,y)
		return "Winner!"

	def calculate_view(self,x,y):
		queue = collections.deque()
		queue.append(board[x][y])
		while queue:
			cell = queue.popleft()
			cell.visble = True
			if not cell.count > 0:
				queue.extend(cell.neighbours) 
		return board

class Cell:
	def __init__(self,bomb=False,count=0):
		self.bomb = bomb
		self.count = 0
		self.neighbours = []
		self.visible = False

	def __repr__(self):
		if self.bomb:
			return "*"
		else:
			return str(self.count)

# File System
class Ex11_Folder:
	def __init__(self, name, parent=None):
		self.parent = parent
		self.contains = []
		self.name = name

class File:
	def __init__(self, parent, data, name):
		self.parent = parent
		self.data = data
		self.name = name

	def get_file_path(self):
		grandparent = self.parent
		file_path = grandparent.name + "/" + self.name
		while grandparent.parent != None:
			grandparent = grandparent.parent
			file_path = grandparent.name + "/" + file_path
		return "/" + file_path

# Hash Table
class Ex12_Hash_Table:
	def __init__(self):
		self.table = [[None for x in range(10)] for y in range(10)] 

	def hash_function(self, data):
		return int(data)

	def add_to_table(self, data):
		position = self.hash_function(data)
		chain_position = self.hash_function(data)
		self.table[position][chain_position] = data

	def retrieve(self, data):
		position = self.hash_function(data)
		chain_position = self.hash_function(data)
		return self.table[position][chain_position]
