"""УГАДАЙКА"""
import random

def is_valid(n): #проверка на правильное заполнение
	return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100


def input_num(): #Вводим значение
	while True:
		guess = input()
		if is_valid(guess):
			return int(guess)
		else:
			print('Нужно ввести целое число от 1 до 100')


def compare_num(first, last): #Сравнение
	num = random.randint(first, last)
	total = 0
	while True:
		n = input_num()
		total += 1
		if n < num:
			print('Попробуйте ввести число побольше')
		elif n > num:
			print('Переборщили, попробуйте ввести число поменьше')
		else:
			print(f'Поздравляю! Вы отградали число за {total} попыток!')
			break

def continue_game(): #Продолжение игры
	answer = input('Хотите продолжить ("д"/"н")?\n')
	while True:
		if answer not in ('y', 'n', 'д', 'н'):
			print('Введите допустимое значение...\n Продолжим ("д"/"н")?\n')
		elif answer in ('n', 'н'):
			print('Отличная была игра! Ещё увидимся!')
			return False
		else:
			return True
def game(): #Запуск игры
	print('Добро пожаловать в числовую угадайку!\nВведите число от 1 до 100:')
	while True:
		print('Для игры укажите диапазон целых чисел от 1 до 100:')
		x, y = input_num(), input_num()
		if x > y:
			x, y = y, x
		print(f'Введите число от {x} до {y}:')
		compare_num(x, y)
		if continue_game():
			continue
		else:
			break

game() #Вызов игры