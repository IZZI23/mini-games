# first python project,rolling dice mini-game

import random

def roll_a_dice():
	while True:
		start = input("would you like to roll a dice?")
		if start.lower() == "y":
			dice = random.randint(1,12)
			print(dice)
		elif start.lower() == "n":
			print("bye")
			break
		else:
			print("not a valid answer!")

roll_a_dice()










# Experementing with Classes,building shop protorype

class Clothes:
	discount = 1
	current_year = 2022
	r = 10

    #MAIN INFO
	def __init__(self, country, year, material, size, price, color, brand):
		self.country = country
		self.year = year
		self.material = material
		self.size = size
		self.price = price
		self.color = color
		self.brand = brand

		



    #PRICE DEPRECIATION
	from math import pow
 
	def depreciation(self):
		t = self.current_year - int(self.year)
		self.price = int(self.price) * pow((1 - self.r / 100), t)
		
		return self.price
		


        
 	# DISCOUNT
	def dis(self):
		self.price = int(self.price) * self.discount	




    #FULL INFORMATION OF THE PRODUCT
	def fullinfo(self):
		return "{} {} {} {} {} ".format(self.country, self.year, self.material, self.size, self.price)




 #NEW CLASS WOMEN
class Women(Clothes):
	r = 30 
	discount = 0.65   

	



    #NEW CLASS MEN
class Men(Clothes):
	r = 15
	discount = 0.85 





#NEW CLASS BABIES 
class Babies(Clothes):
	r = 5
	discount = 0.80
 



cl_1 = Women("France", "2015", "Synthetic", "S,M,L", "133","White","Nike")
cl_2 = Women("Spain", "2018", "Cotton", "XS,L,XL", "91", "Red", "Prada" )
cl_3 = Men("Azerbaijan", "2020", "Wool", "M,L,XL", "55", "Blue", "Zara")
cl_4 = Men("Italy", "2021", "Silk", "M,XL", "243", "Black", "Adidas")
cl_5 = Babies("Russia", "2016", "Leather", "XS,S,M,L,2XL", "109", "Red", "Chico")
cl_6 = Babies("China", "2019", "Synthetic ", "XS,S,M,L,XL,2XL", "43", "Green", "Tuzama")



print(cl_6.brand)
print(cl_3.material)
print(cl_5.color)
print(cl_1.price)
cl_1.dis()
print(cl_1.price)

print(cl_2.depreciation())











# Fucking tic tac toe Game,Tutorial Based.

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

			#Horizontal
def win (current_game):
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player{row[0]} is a winner horizontally---")

			#Diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player{diags[0]} is a winner dioganally/")

			# Diagonal
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player{diags[0]} is a winner dioganally\\")

		
			#Vertical
	for col in range(len(game)):
		check=[]

		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0:
			print(f"Player{check[0]} is a winner vertically|")

				#GAME BOARD

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		print("   a  b  c")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		
		return game_map	
	except IndexError as e:
		print("Eror: make sure input row/column as 0,1,2?", e)
	except Exception as e:
		print("something went wrong!!")		



play= True
players= [1, 2]
while play:
	game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0],]
	
	game_won = False
	game = game_board(game, just_display=True)
	while not game_won:
		current_player = 1
		column_choice = int(input("what column do you want to play? (0,1,2):  "))
		row_choice = int(input("what row do you want to play? (0,1,2):  "))
		game = game_board(game, current_player, row_choice, column_choice)






game= game_board(game, just_display=True)
game= game_board(game, player=1, row=1, column=1)
