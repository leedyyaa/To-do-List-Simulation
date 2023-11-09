#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:16:28 2022

@author: lydiakim
"""
from tasks import *

############################
# check_option
my_menu0 = {}
my_menu1 = {1: "One"}
my_menu2 = {'L': "List"}

result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`\n")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`\n")
assert result == "valid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu2)
print(f"--> check_option('1', my_menu2) returned `{result}`\n")
assert result == "invalid"

result = check_option('L', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "valid"    


############################
# validate_date
assert validate_date('01/12/2022') == True
# print(validate_date('01/12/2022')[1])
# assert validate_date('01/12/2022')[1] == '01/12/2022'

assert validate_date('01/44/2022') == False
# assert validate_date('01/44/2022')[1] == -4

assert validate_date('January/12/2022') == False
# assert validate_date('January/12/2022')[1] == -2


############################
# is_valid_index
assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True


############################
# is_numeric
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5')
print(f"--> is_numeric('5.5') returned `{result}`")
assert result == True

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False


############################
# create_a_task
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[0] == True
assert type(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]) == dict
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['name'] == 'do dishes'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['description'] == 'wash the plates from dinner'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['deadline'] == '03/04/2022'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'] == 2
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'] == False

# Regular input 2
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[0] == True
assert type(create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]) == dict
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['name'] == 'see endgame'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['description'] == 'endgame with friends saturday'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['deadline'] == '01/18/2020'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['priority'] == 3
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['completed'] == True

# name too short
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[1] == 'name'

# name too long
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[1] == 'name'

# description empty
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[1] == 'description'

# invalid dates empty
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[1] == 'deadline'

# invalid priority
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[1] == 'priority'

# invalid completion
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[1] == 'completed'


############################
# update_task
# for testing purposes, so you can observe the output
my_list = [{
    'name': 'get groceries',
    'description': 'buy some jam and peanut butter',
    'deadline': '02/23/2022',
    'priority': 2,
    'completed': False
    },
    {
    'name': 'get some sleep',
    'description': '8 hours of sleep is necessary',
    'deadline': '02/03/2022',
    'priority': 3,
    'completed': True
    },
    {
    'name': 'compar. lit essay',
    'description': "finish comparative lit essay that's overdue",
    'deadline': '02/15/2022',
    'priority': 4,
    'completed': True
    }]

result = update_task(my_list, '5', 'name', 'go clubbing')
assert result[1] == "idx"
assert result[0] == False
print("--> update_task(my_list, '5', 'name', 'go clubbing') "+
      f"successfully returned error with `{result[1]}`\n")

result = update_task(my_list, '1', 'Get Gift', 'I\'m quite hungry though')
assert result[1] == "field" # returned idx
assert result[0] == False
print("--> update_task(my_list, '1', 'Get Gift', 'I\'m quite hungry though') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, '1', 'deadline', 'never')
assert result[1] == "deadline"
assert result[0] == False
print("--> update_task(my_list, '1', 'deadline', 'never') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, '1', 'priority', 'pants on FIRE!!!!')
assert result[1] == "priority"
assert result[0] == False
print("--> update_task(my_list, '1', 'priority', 'pants on FIRE!!!!') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, '1', 'priority', '5')
print(result[1]['priority'])
assert result[1]['priority'] == '5'
assert result[0] == True
print("--> update_task(my_list, '1', 'priority', '5') "+
      f"successfully returned error with `{result[1]['priority']}`\n")


result = update_task(my_list, '1', 'completed', 'technically, yes')
assert result[1] == "completed"
assert result[0] == False
print("--> update_task(my_list, '1', 'completed', 'technically, yes') "+
      f"successfully returned error with `{result[1]}`\n")


result = update_task(my_list, '1', 'deadline', '01/22/19')
assert result[0] == True
assert result[1]['deadline'] == '01/22/19'
print("--> update_task(my_list, '1', 'Deadline', '01/22/19' "+
      f"successfully returned updated task: \n{result[1]['deadline']}\n")

result = update_task(my_list, '1', 'completed', 'no')
assert result[0] == True
assert result[1]['completed'] == False
print("--> update_task(my_list, '1', 'completed', 'no') "+
      f"successfully returned updated task: \n{result[1]['completed']}\n")



############################
# load_from_csv
result = load_from_csv("task_data.csv")
print(f"load_from_csv('task_data.csv') returned:\n{result}")
assert type(result) == list
assert type(result[0]) == dict
assert result[1]['name'] == "Do labs"
assert result[0]['deadline'] == "01/22/2022"
  

result = load_from_csv("task_data2.csv")
print(f"load_from_csv('task_data2.csv') successfully returned:\n'{result}'\n")
assert type(result) == str
assert result == "invalid data"

result = load_from_csv("task_data3.csv")
print(f"load_from_csv('task_data3.csv') successfully returned:\n'{result}'\n")
assert type(result) == str
assert result == "inconsistent format"








