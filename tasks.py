#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:13:35 2022

@author: lydiakim
"""
from validate import *

import csv

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and to output a question
    "What would you like to do?"
    """
    print("**************************")
    print("What would you like to do?")
    for key in menu:
        print("{} - {}".format(key, menu[key]))
    print("**************************")

def check_option(option, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided collection.
    Otherwise, return "invalid".
    """
    if option in menu:
        return "valid"
    else:
        return "invalid"
    
def create_a_task(name, description, date, priority, completed):
    '''
    validate each parameter starting from "name" and until "completed"
    If one of them fails, return (False, <name of parameter>)
    ex. (False, "name") if "name" is not 3-15 characters long
    or (False, "completed") if completed is not a "yes" or "no"
    If all validations pass, return (True, <dictionary with fields name, description...>)
    '''
    if validate_name(name)==False:
        return False, 'name'
    if validate_description(description)==False:
        return False, 'description'
    if validate_date(date)==False:
        return False, 'deadline'
    if validate_priority(priority)==False:
        return False, 'priority'
    if validate_completed(completed)==False :#validate update using the correct function call(s)
        return False, 'completed' #TODO: return the necessary tuple
    else:
        if completed.upper()=='NO':
            completed=False
        elif completed.upper()=='YES':
            completed=True
    dict = {'name': name, 'description': description, 'deadline':date, 'priority':int(priority), 'completed':completed}
    return True, dict

def slashes_to_written(date_list):
    '''
    given a date in the month/day/year format,
    output a string in the written format
    '''
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = ''
    day = 0
    if type(date_list)==list:
        year = date_list[2]
        # Finish the function
        for x in month_names:
            if x == int(date_list[0]):
                month = month_names[x]
        day = int(date_list[1])
    if type(date_list)==str:
        y = date_list.split('/')
        year = y[2]
            # Finish the function
        for x in month_names:
            if x == int(y[0]):
                month = month_names[x]
        day = int(y[1])
    
    # Return the date string in written format
    return (f'{month} {day}, {year}')

def priorityFormat(num):
    '''
    given a number, output its written correspondent

    '''
    if num == 1:
        return 'Lowest'
    elif num == 2:
        return 'Low'
    elif num == 3:
        return 'Medium'
    elif num == 4:
        return 'High'
    elif num == 5:
        return 'Highest'
        
def complete(num):
    '''
    given a boolean value, output its written correspondent
    '''
    if num==False:
        return 'No'
    elif num==True:
        return 'Yes'
    
def print_formatted_tasks(tasks_list):
    '''
    given a list of tasks, print them in a formatted manner

    '''
    # Finish the function definition
    index=0
    for task in tasks_list: # task - each dictionary
        for t in task: # t - each key in dictionary
            tt = task.copy()
            if t == 'name':
                print(f'{index}:  {task[t].upper()}')
            elif t == 'deadline':
                t == 'priority'
                task['deadline'] == tt['priority']
                print(f'    {"priority".capitalize()}: {priorityFormat(task["priority"])}')
            elif t == 'completed':
                print(f'    {t.capitalize()}: {complete(task[t])}')
            elif t == 'priority':
                t == 'deadline'
                task['priority'] == tt['deadline']
                print(f'    {"deadline".capitalize()}: {slashes_to_written(task["deadline"])}')
            else:
                print(f'    {t.capitalize()}: {task[t]}')
        index+=1
        print()
        
def print_tasks_by_status(all_tasks, completed=False):
    """
    Prints tasks from 'all_tasks',
    based on the value of 'completed' of each task.
    If there are no tasks that are incomplete,
    prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed,
    prints 'You do not have completed tasks.'
    Otherwise, prints the requested tasks.
    """
          
    incomplete=[]
    complete=0
    
    if len(all_tasks)==0:
        if completed==False:
            print('You do not have incomplete tasks.')
        elif completed==True:
            print('You do not have completed tasks.')
            
    elif len(all_tasks)==1:
        for task in all_tasks:
            for x in task:
                if task[x] != False and completed==True:
                    complete+=1
                elif task[x] == False and completed==False:
                    incomplete.append(task[x])
        if complete>0:
            print('You do not have incomplete tasks.')
            print_formatted_tasks(all_tasks)
        else:
            print('You do not have completed tasks.')
            print(incomplete)
    
def update_task(task_list, task_id, task_field, task_update):
    """ Given
    * the task list (`task_list`)
    * the task index that has been selected (`task_id`)
    * the field of the selected task (`task_field`)
    * the updated information (`task_update`)
    Validate the parameters to check for syntax and structure. 
    If all validations passed, return a tuple with a boolean True and 
    the updated task (a dictionary from the `task_list` at the provided `task_id`).
    Ff validations fail, return a tuple with a boolean False and 
    a string with the task_field that caused the error during validation.
    """

    fields = [
    'name',
    'description',
    'deadline',
    'priority',
    'completed'
    ] #you may use this to validate field_name

    if is_valid_index(int(task_id), task_list)==False:
        return False, 'idx'
    if task_field == 'name': # use the correct function call(s)
        if validate_name(task_update)==False :#validate update using the correct function call(s)
            return False, 'name' #TODO: return the necessary tuple
        else:
            task_list[int(task_id)][task_field]=task_update
            return True, task_list[int(task_id)]
            #TODO: update the task list accordingly
    elif task_field == 'description': # use the correct function call(s)
        if validate_description(task_update)==False :#validate update using the correct function call(s)
            return False, 'description' #TODO: return the necessary tuple
        else:
            task_list[int(task_id)][task_field]=task_update
            return True, task_list[int(task_id)] #TODO: continue checking the next field
    elif task_field == 'priority': # use the correct function call(s)
        if validate_priority(task_update)==False :#validate update using the correct function call(s)
            return False, 'priority' #TODO: return the necessary tuple
        else:
            task_list[int(task_id)][task_field]=task_update
            return True, task_list[int(task_id)]
    elif task_field == 'deadline': # use the correct function call(s)
        if validate_date(task_update)==False :#validate update using the correct function call(s)
            return False, 'deadline' #TODO: return the necessary tuple
        else:
            task_list[int(task_id)][task_field]=task_update
            return True, task_list[int(task_id)]
    elif task_field == 'completed': # use the correct function call(s)
        if validate_completed(task_update)==False :#validate update using the correct function call(s)
            return False, 'completed' #TODO: return the necessary tuple
        else:
            if task_update.upper()=='NO':
                task_update=False
            elif task_update.upper()=='YES':
                task_update=True
            task_list[int(task_id)][task_field]=task_update
            return True, task_list[int(task_id)]
    else:
        return False, 'field'
    # return task_list #TODO: return the proper value if all validations passed
    
def delete_task(idx, tasks):
    """
    Checks if idx, which is an integer, is a valid index inside Tasks
    If not, returns False
    If a valid index, removes the element at index 'idx'
      from tasks, and returns True
    """
    if idx in range(len(tasks)):
        tasks.pop(idx)
        return True
    else:
        return False
    
def print_sorted_priority(all_tasks):
    """
    Prints tasks from all_tasks, but sorted by priority,
    highest priority first
    """
    highestP = 0
    if len(all_tasks) == 1:
        print(all_tasks)
    if len(all_tasks) > 1:
        for dic in all_tasks:
            if dic['priority'] > highestP:
                highestP = dic['priority']
        print(dic)
        all_tasks.remove(dic)
        print_sorted_priority(all_tasks)
 
def save_to_csv(my_list, filename):
    '''
    accepts the list with nested dictionaries and the string with the 
    filename to which to save it.
    '''
    #f = open('file.txt', 'w') 
    with open(filename, 'w', newline='') as f:
        task_writer = csv.writer(f)
        task_data = []
        for dic in my_list:
            for key in dic: 
                task_data.append(dic[key])
            #task_data.append('\n')
            task_writer.writerow(task_data)
            task_data.clear()

def load_from_csv(filename):
    '''
    Reads the csv file and creates a new list of tasks using
    the data in that file. Loop through the lines of data and 
    in each iteration, call create_a_task() to get the data 
    as a dictionary. Save each valid dictionary into the list 
    tasks (i.e., dictionaries).
    Note that this function is responsible for converting
    the last (Boolean) field of the task from "True"/"False"
    to "yes"/"no", so that the task can be correctly created
    using the create_a_task() function.

    Return the resulting list of dictionaries, which will be 
    empty, if the file is empty or the data in it is invalid.
    '''
    
    new_list = [] # empty list to store the data from the csv file
    
    with open(filename, 'r', newline='') as csvfile:
        reader_object = csv.reader(csvfile) #TODO: initiate csv.reader object

        for values in reader_object:
            if len(values)==5: #check if there are 5 items in the list 'values'
                
                #convert the last field (a Boolean flag) to "yes" or "no"
                if values[4] == False:
                    values[4]='no'
                elif values[4] == True:
                    values[4]='yes'
                #call create_task_task and add it to new_list
                result = create_a_task(values[0],values[1],values[2],values[3],values[4]) #TODO: FILL ME IN
                # print(result)
                if result[0] == True:#TODO: checks what create_a_task returned
                    new_list.append(result[1])#TODO: append the dictionary to the new_list
                else:
                    print("WARNING: invalid data -", values)
                    return "invalid data"

            else: #if data formatting is inconsistent
                print("WARNING: invalid data -", values)
                print("WARNING: Data formatting is inconsistent with the task manager!")
                return "inconsistent format"

    return new_list




