#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:15:53 2022

@author: lydiakim
"""
from tasks import *

if __name__ == '__main__':
    the_menu = {'P': 'Print tasks',
    'A': 'Add a task',
    'U': 'Update a task',
    'D': 'Delete a task',
    'SI': 'Show incomplete tasks',
    'SC': 'Show completed tasks',
    'SP': 'Show tasks sorted by priority, highest first',
    'SD': 'Show tasks sorted by deadline, earliest first',
    'S': 'Save tasks',
    'L': 'Load tasks from file',
    'Q': 'Quit this program'} #TODO: add the menu options from the instructions

    opt = None
    tasksList = []
    while True:
        print_main_menu(the_menu) #TODO
        print("::: Enter an option")
        opt = input("> ")

        if opt.upper() == 'Q': #TODO: make Q or q quit the program
            print("See you next time!")
            break # exit the main `while` loop
        else:
            if check_option(opt.upper(), the_menu) == "invalid": #TODO
                print('Invalid option, please try again')
            print(f"You selected option {opt.upper()} to > {the_menu[opt.upper()]}.")
            
        if opt.upper() == 'P': #TODO
            if len(tasksList)==0:
                print('There are currently no tasks!')
            else:
                
                print_formatted_tasks(tasksList)
            
        elif opt.upper() == 'A': #TODO
            print("::: Enter the task name")
            name = input("> ")
            print("::: Enter the task description")
            description = input("> ")
            print("::: Enter the task deadline")
            date = input("> ")
            print("::: Enter the priority on a scale of 1-5")
            priority = input("> ")
            print("::: Have you completed the task?")
            completed = input("> ")
            tasksList.append(create_a_task(name, description, date, priority, completed)[1])
            if create_a_task(name, description, date, priority, completed)[0] == False:
                print(f'Invalid {create_a_task(name, description, date, priority, completed)[1]} - please try again')
                
        
        elif opt.upper() == 'U': #TODO
            if len(tasksList)==0:
                print('There are currently no tasks!')
            else:
                print("::: Which task would you like to update?")
                taskId = input("> ")
                print("::: Which category would you like to update?")
                field = input("> ")
                print(f"::: Enter the new {field}")
                update = input("> ")
                update_task(tasksList, taskId, field, update)[1]
        
        elif opt.upper() == 'D':
            print("::: Which task would you like to delete?")
            delete = int(input("> "))
            if delete_task(delete, tasksList) == False:
                print('Invalid index')
            else:
                delete_task(delete, tasksList)
                
        elif opt.upper() == 'SI':
            print_tasks_by_status(tasksList, False)
            
        elif opt.upper() == 'SC':
            print_tasks_by_status(tasksList, True)
            
        elif opt.upper() == 'SP':
            print_sorted_priority(tasksList) 
            
        elif opt.upper() == 'S':
            print("::: What would you like to name your file?")
            filename = input("> ")
            save_to_csv(tasksList, filename)
            
        elif opt.upper() == 'L':
            print("::: Which file would you like to load??")
            filename = input("> ")
            load_from_csv(filename)
            
        else:
            print("This option is not yet implemented.") #TODO

        opt = input("::: Press Enter to continue...")

    print("Have a productive day!")
    
    
    
    
    
    
    
    
    
    
    
    