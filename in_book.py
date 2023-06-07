# def two_devision(x):
# 	"""
# 	Возвращает х / 2.
# 	:параметр х: целое число
# 	:return: целочисленное деление х на 2
# 	"""
# 	return int(x / 2)
#
# def four_multiplying(y):
# 	"""
# 	Возвращает y * 4.
# 	:параметр y: целое число
# 	:return: умножение y на 2
# 	"""
# 	return int(y * 4)
#
# my_number = two_devision(4)
# print(four_multiplying(my_number))
import functools

# def to_float(a):
# 	"""
# 	Преобразует строку в число с плавающей точкой.
# 	"""
# 	try:
# 		b = float(a)
# 		return b
# 	except ValueError:
# 		print('Неверный ввод')
#
# text = input()
# print(to_float(text))

# КОЛЛЕКЦИИ (КОНТЕЙНЕРЫ ДАННЫХ): список, кортеж, словарь, множества (замороженные множества)

# my_musicians = ['FKJ', 'Miyagi', 'Andy Panda']
# my_locations = [(51.43413, 32.23412), (32.23412, 34.23123)]
# my_facts = {
# 	'height': 185,
# 	'weight': 85,
# 	'color': 'blue',
# 	'actor': 'Leonardo Di Caprio'
# }
# # your_fact = input()
# # print(my_facts[your_fact])
#
# my_songs = {
# 	'FKJ': ['Tadow', 'YingYang', 'Skyline'],
# 	'Miyagi': ['Captain', 'Половина моя', 'Самурай'],
# 	'Andy Panda': ['King Kong', 'Jumanji', 'Billboard']
# }
#
# my_set = set('from a string')
# private_set = {'Michiagan', 'Florida', 'Washington'}
# print(my_set | private_set)
# print(my_set & private_set)
# print(my_set.symmetric_difference(private_set))
# print(my_set.difference(private_set))
# print(my_set - private_set)
# print(my_set <= private_set)
# print(my_set >= private_set)
# print(private_set <= my_set)
# print(private_set >= my_set)
# print(my_set.issubset(private_set))
# print(my_set.issuperset(private_set))
# print(my_set.isdisjoint(private_set))
# x = frozenset([1, 2, 3, 4, 5])
# y = x.copy()
# print(y)

# СТРОКИ

author = 'Чехов'
# for i in author:
# 	print(i)

# first_ans = input()
# sec_ans = input()
# print('Вчера я написал {}. Вчера я ходил в {}'.format(first_ans, sec_ans))

# text = 'олдос Хаскли что-то там'
# print(text.title())

# text = 'Where is it? Who is it? When is it?'
# new_text = text.split('?')
# print(new_text)

# text = ['White', 'fox', 'jumped', 'out', 'of', 'space', '.']
# new_text = ' '.join(text[0:6]) + text[-1]
# print(new_text)

# text = 'Child is a mirror of parents\' acts'
# new_text = text.replace('o', '0')
# print(new_text)

# text = 'Hamminguai'
# print(text.index('m'))

# print("'Who is it?' said my frind")

# text = 'три'
# print(text * 3)

# text = 'Only me and you understand who is who! Let me talk to you.'
# splitter = text.index('!')
# print(text[0:splitter])

# ЦИКЛЫ

# qs = ['What\'s your name?\n', 'How old are you?\n', 'Where are you from?\n']
# n = 0
# while True:
# 	print('Enter X to exit')
# 	a = input(qs[n].lower())
# 	if a == 'x':
# 		break
# 	n = (n + 1) % 3

# tv_shows = ['Walking Dead', 'Doctor House', 'Friends']
# for i, value in enumerate(tv_shows):
# 	a = '{}: {}'.format(i+1, value)
# 	print(a)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# while True:
# 	answer = input('Guess a number! Press "X" to exit.\n').lower()
# 	if answer == 'x':
# 		break
# 	try:
# 		answer = int(answer)
# 	except ValueError:
# 		print('You must to enter integer number or press "X" to exit.\n')
# 	if answer in numbers:
# 		print('Congrats!')
# 	else:
# 		print('Try again!')

# num1 = [1, 2, 3, 4, 5]
# num2 = [3, 4, 1, 2, 5]
# res = list()
# for i in num1:
# 	for j in num2:
# 		res.append(i * j)
# print(res)

# МОДУЛИ

# import statistics
# numbers = [1, 2, 3, 4, 5, 6]
# a = statistics.mean(numbers)
# print(a)

# import cubes
# print(cubes.to_cube(5))

# ФАЙЛЫ
# import os
# os.path.join('D', 'Documents', 'Python', 'start_time', 'сам себе программист')

# st = open('test.py', 'w')
# st.write('print(Hello World!)')
# st.close()

# with open('testing.py', 'w') as f:
# 	f.write('This is testing!')

# with open('testing.py', 'r') as g:
# 	print(g.read())

# test_list = list()
# with open('testing.py', 'r') as j:
# 	test_list.append(j.read())
#
# print(test_list)

# import csv
# with open('test.csv', 'w') as k:
# 	w = csv.writer(k, delimiter=',')
# 	w.writerow(['one',
# 	            'two',
# 	            'three',
# 	            'four',
# 	            'five',
# 	            'six'])

# import csv
# with open('test.csv', 'r') as l:
# 	r = csv.reader(l, delimiter=',')
# 	for row in r:
# 		print(', '.join(row))

# import os.path
# test_path = os.path.join('Self_Taught_Programmer_Althoff', 'Глава 2', 'chap2_challenge1.py')
#
# with open(test_path, 'r') as i:
# 	print(i.read())

# smthg = input()
# with open('testing.py', 'w') as l:
# 	l.write(smthg)

# import csv
# films = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# with open('test.csv', 'w') as k:
# 	w = csv.writer(k, delimiter=',')
# 	for row in films:
# 		w.writerow(row)

# ВИСЕЛИЦА

# def hangman(word):
# 	wrong = 0
# 	stages = ["",
# 	          "_________       ",
# 	          "|       |       ",
# 	          "|       O       ",
# 	          "|      /|\      ",
# 	          "|      / \      ",
# 	          "|               "
# 	          ]
# 	rletters = list(word)
# 	board = ["_"] * len(word)
# 	win = False
# 	print('Добро пожаловать в игру!')
#
# 	while wrong < len(stages) - 1:
# 		msg = 'Введите букву: '
# 		char = input(msg)
# 		if char in rletters:
# 			cind = rletters.index(char)
# 			board[cind] = char
# 			rletters[cind] = '$'
# 		else:
# 			wrong += 1
# 		print(" ".join(board))
# 		e = wrong + 1
# 		print('\n'.join(stages[0:e]))
# 		if "_" not in board:
# 			print(f'Вы выжили! Было загадано слово: {"".join(board)}')
# 			win = True
# 			break
# 	if not win:
# 		print('\n'.join(stages[0:wrong+1]))
# 		print('Вы проиграли! Было загадано слово: {} '.format(word))
#
# import random
# words_for_game = ['кошка', 'котенок', 'лопата', 'звезда']
# hangman(random.choice(words_for_game))

# ООП

# class People:
# 	def __init__(self, h, w):
# 		self.weight = w
# 		self.height = h
# 		self.jurk = False
# 		print('Новый человек!')
#
# 	def chert(self, actions):
# 		if actions == 'Лох':
# 			self.jurk = True
#
# human1 = People(185, 85)
# print(human1.jurk)
# human1.chert('Лох')
# print(human1.jurk)

# class Rectangle():
# 	def __init__(self, w, l):
# 		self.width = w
# 		self.len = l
#
# 	def area(self):
# 		return self.width * self.len
#
# 	def change_size(self, w, l):
# 		self.width = w
# 		self.len = l
#
# rectangle = Rectangle(5, 6)
# print(rectangle.area())
# rectangle.change_size(7, 8)
# print(rectangle.area())

# class Apples():
# 	def __init__(self, w, col, s, con):
# 		self.weight = w
# 		self.color = col
# 		self.sort = s
# 		self.condition = con
#
# my_apple = Apples(50, 'red', 'prince', 'fresh')
# print(my_apple.__dict__)

# from math import pi
#
# class Circles():
# 	def __init__(self, r):
# 		self.radius = r
#
# 	def area(self):
# 		return pi * (self.radius**2)
#
# my_circle = Circles(5)
# print(my_circle.area())

# from math import sqrt
#
# class Triangles():
# 	def __init__(self, a, b, c):
# 		self.a = a
# 		self.b = b
# 		self.c = c
#
# 	def area(self):
# 		p = (self.a + self.b + self.c) / 2
# 		return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
# my_triangle = Triangles(5, 6, 7)
# print(my_triangle.area())

# class Hexagon():
# 	def __init__(self, a):
# 		self.a = a
#
# 	def area(self):
# 		return self.a * 6
#
# my_hexagon = Hexagon(5)
# print(my_hexagon.area())

# ЧЕТЫРЕ СТОЛПА ООП

# class Shape():
# 	def what_am_i(self):
# 		print('I am a shape')
#
# class Rectangle(Shape):
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
#
# 	def calculate_perimeter(self):
# 		return self.a * 2 + self.b * 2
#
# class Square(Shape):
# 	square_list = []
#
# 	def __init__(self, a):
# 		self.a = a
# 		self.square_list.append(self)
#
# 	def __repr__(self):
# 		return (f'{self.a} на {self.a} на {self.a} на {self.a}')
#
# 	def calculate_perimeter(self):
# 		return self.a * 4
#
# 	def change_size(self, new_size):
# 		self.a += new_size
#
# test_square = Square(5)
# copied_square = test_square
#
# def the_same_object(a, b):
# 	return a is b
#
# print(the_same_object(test_square, copied_square))

# class Rider():
# 	def __init__(self, name):
# 		self.name = name
#
# class Horse():
# 	def __init__(self, color, owner):
# 		self.color = color
# 		self.owner = owner
#
# first_rider = Rider('Maxim Glushko')
# first_horse = Horse('red', first_rider)
# print(first_horse.owner.name)

# ПЬЯНИЦА

# class Card():
# 	suits = ["қарға", "қызылайыр", "боб", "крешь"]
#
# 	values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', "дама", "король", "туз"]
#
# 	def __init__(self, v, s):
# 		"""v and s are integers"""
# 		self.value = v
# 		self.suit = s
#
# 	def __lt__(self, c2):
# 		if self.value < c2.value:
# 			return True
# 		if self.value == c2.value:
# 			if self.suit < c2.suit:
# 				return True
# 			else:
# 				return False
# 		return False
#
# 	def __gt__(self, c2):
# 		if self.value > c2.value:
# 			return True
# 		if self.value == c2.value:
# 			if self.suit > c2.value:
# 				return True
# 			else:
# 				return False
# 		return False
#
# 	def __repr__(self):
# 		r = f'{self.values[self.value]} - {self.suits[self.suit]}'
# 		return r
#
# from random import shuffle
#
# class Deck():
# 	def __init__(self):
# 		self.cards = []
# 		for i in range(2, 15):
# 			for j in range(4):
# 				self.cards.append(Card(i, j))
# 		shuffle(self.cards)
#
# 	def rm_card(self):
# 		if len(self.cards) == 0:
# 			return
# 		return self.cards.pop()
#
# class Player():
# 	def __init__(self, name):
# 		self.wins = 0
# 		self.card = None
# 		self.name = name
#
# class Game():
# 	def __init__(self):
# 		name1 = input('Бірінші ойыншының аты: ')
# 		name2 = input('Екінші ойыншының аты: ')
# 		self.deck = Deck()
# 		self.p1 = Player(name1)
# 		self.p2 = Player(name2)
#
# 	def wins(self, winner):
# 		w = f'{winner} забирает карты'
# 		print(w)
#
# 	def draw(self, p1n, p1c, p2n, p2c):
# 		d = f'{p1n} кладет {p1c}, а {p2n} кладет {p2c}'
# 		print(d)
#
# 	def play_game(self):
# 		cards = self.deck.cards
# 		print('Ал кеттік!')
# 		while len(cards) >= 2:
# 			response = input('Шығу үшін Х басыңыз. Ойынды бастау үшін кез-келген басқа батырманы басыңыз').lower()
# 			if response == 'x' or response == 'х':
# 				break
# 			p1c = self.deck.rm_card()
# 			p2c = self.deck.rm_card()
# 			p1n = self.p1.name
# 			p2n = self.p2.name
# 			self.draw(p1n, p1c, p2n, p2c)
# 			if p1c > p2c:
# 				self.p1.wins += 1
# 				self.wins(self.p1.name)
# 			else:
# 				self.p2.wins += 1
# 				self.wins(self.p2.name)
# 		win = self.winner(self.p1, self.p2)
#
# 		print(f'Ойын бітті! {win} жеңді!')
#
# 	def winner(self, p1, p2):
# 		if p1.wins > p2.wins:
# 			return p1.name
# 		if p1.wins < p2.wins:
# 			return p2.name
# 		return 'Тепе-теңдік!'
#
# my_game = Game()
# my_game.play_game()

#BASH, WSL, РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

# import re
# l = 'Beautiful better than ugly'
# matches = re.findall('beautiful', l, re.IGNORECASE)
# print(matches)

# import re
# d = """Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# __what__ __is__ __your__ __name__"""

# m = re.findall("__.*?__", d, re.MULTILINE)
# for match in m:
# 	print(match)

# ЧЕПУХА

# import re
#
# text = """What is __ABRA__ name? Who is __ABRA__? You're a __VERB__! Give me a __LOTUS__!"""
#
# def mad_libs(mls):
# 	hints = re.findall("__.*?__", mls)
#
# 	if hints is not None:
# 		for word in hints:
# 			q = input(f'Введите {word}')
# 			mls = mls.replace(word, q, 1)
# 		print('\n')
# 		mls = mls.replace('\n', '')
# 		print(mls)
# 	else:
# 		print('Ошибка ввода!')
# mad_libs(text)

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
# 	return "Hello World!"
#
# app.run(port=8000)

