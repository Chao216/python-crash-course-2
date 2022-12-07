import os

print(f'\nThe current working directoy is: {os.getcwd()}')

os.chdir('../')

print(f'\nThe current working directoy is: {os.getcwd()}')
