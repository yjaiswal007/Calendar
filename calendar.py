# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:31:44 2020

@author: Yash D. Jaiswal & Divya D. Jaiswal
"""


import numpy as np
import pandas as pd


def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

def fill_month(year):
    months = [[] for _ in range(7)]  # initialize

    ref_year, ref = 2000, 6  # starting day --> 6

    # estimate shifting needed
    if year > ref_year:
        delta = year - ref_year - 1
        shift = 2 + (delta*1 + (delta//4) - (delta//100) + (delta//400))%7
    elif year < ref_year:
        delta = ref_year - year
        shift = 7 - ((delta*1 + (delta//4) - (delta//100) + (delta//400))%7)
    else:
        shift = 0
    
    ref = (ref + shift) % 7
    
    day_dict = {0: 'sun', 1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat'}
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    month_dict = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 
                  'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 
                  'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
    
    # identify position of every month based on year and shifts
    for mnt in month_list:    
        months[ref].append(mnt)
        
        if mnt == 'Feb':
            if check_leap_year(year):
                ref = (ref + 1 + month_dict[mnt]) % 7
        else:
            ref = (ref + month_dict[mnt]) % 7
            
    return months

if __name__ == '__main__':
    
    start_year = int(input('Enter the start year: '))
    end_year = int(input('Enter the end year: '))
    
    for year in range(start_year, end_year + 1):
        months = fill_month(year)
        print(months)
    
      