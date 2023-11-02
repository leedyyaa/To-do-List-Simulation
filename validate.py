#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:12:44 2022

@author: lydiakim
"""

def check_option(option, menu):
    """
    Given an option, return "valid" if it is
    of type str and is a valid key in
    the provided collection.
    Otherwise, return "invalid".
    """
    '''
    for x in menu:
        if isinstance(option, str) and option == x:
            return 'valid'
        else:
            return 'invalid'
    '''
    if type(option) == str and option in menu:
        return "valid"
    return "invalid"

def is_numeric(val):
    """
    Returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    count=0
    for x in val:
        if x == '.':
            count+=1
        elif not x.isdigit():
            return False
            break
        
    if count>=2:
        return False
    else:
        return True
    
def is_valid_index(idx, in_list):
    """
    Checks whether the provided index `idx`
    is a valid positive index that can retrieve
    an element from `in_list`.
    Returns False if `idx` is negative or exceeds
    the size of `in_list` - 1.
    """
    if idx in range(len(in_list)):
        return True
    else:
        return False
    
def validate_name(name):
    '''
    validates the "name" parameter
    Returns True if the name is between 3 and 15 characters long, inclusive
    Returns False otherwise
    '''
    if len(name)>=3 and len(name)<=15:
        return True
    else:
        return False

def validate_description(desc):
    '''
    validates the "desc" parameter
    Returns True if desc is a non-empty string
    Returns False otherwise
    '''
    if desc != '':
        return True
    else:
        return False

def validate_date(date_string):
    '''
    validate the "date_string"
    Returns True if date_string is a valid date string
    in slashes format (lab 8.16)
    Returns False otherwise
    '''
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    splitS = date_string.split('/')
    if len(splitS) != 3:
        return False
    for num in splitS:
        if not num.isdigit():
            return False
    if int(splitS[0])<1 or int(splitS[0])>12:
        return False
    # if len(splitS[2]) != 4: # if year is not 4 digits
    #     return False
    for x in num_days:
        if x == int(splitS[0]):
            if int(splitS[1])>num_days[x] or int(splitS[1])<1:
                return False
    return True


def validate_priority(priority):
    '''
    validate the "priority" parameter
    Returns True if "priority" is a string containing a number 1-5
    Returns False otherwise
    '''
    num = ['1','2','3','4','5']
    if priority in num and type(priority)==str:
        return True
    else:
        return False
        
# print(validate_priority('7')) # false

def validate_completed(comp):
    '''
    validate the "comp" parameter.
    Returns True if s is one of: "yes", "no", "Yes", "No"
    Returns False otherwise
    '''
    if comp.upper()=='YES' or comp.upper()=='NO':
        return True
    else:
        return False