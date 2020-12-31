# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:22:36 2020

@author: Yash D. Jaiswal & Divya D. Jaiswal
"""


import io
import matplotlib.pyplot as plt
from PIL import Image


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

def generate_calendar(months, year):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    fig = plt.figure(figsize = (13,9))
    ax = fig.add_subplot(111)
    
    x = 0.01
    y = 0.7
    for i in range(1,32):
        # Write dates
        if (check_leap_year(year)) & (i == 29):
            date_color = 'magenta'
        elif (i == 28) &  (not check_leap_year(year)):
            date_color = 'magenta'
        elif i == 30:
            date_color = 'darkgoldenrod'
        elif i == 31:
            date_color = 'forestgreen'
        else:
            date_color = 'blue'
            
        ax.annotate(str(i), xy=(x,y), xycoords='data', 
            fontsize=12, fontweight='bold', color = date_color)
        
        y -= 0.1
        if i%7 == 0:
            x += 0.06
            y = 0.7
    
    # Write days
    x = 0.01 + 0.06*6
    y = 0.7
    for i in range(7):
        for day in days[i:] + days[:i]:
            if (day == 'Sun'):
                color_day = 'red'
            elif (day == 'Sat'):
                color_day = 'maroon'
            else:
                color_day = 'teal'
            ax.annotate(day, xy=(x,y), xycoords='data', 
                fontsize=12, fontweight='bold', color = color_day)
            y -= 0.1
        x += 0.08
        y = 0.7
    
    ax.annotate(str(year), xy=(0.05,0.87), xycoords='data', 
        fontsize=50, fontweight='bold', color = 'black')
    ax.annotate('(Distinct color indicates last date in a month)', xy=(-0.01,0.78), 
        xycoords='data', fontsize=10, fontweight='light', fontstyle='italic', color = 'black')
    
    # Write months
    x = 0.01 + 0.06*6
    mnt30 = ['Apr', 'Jun', 'Sep', 'Nov']
    for mnt in months:
        y = 1
        for mn in mnt:
            if mn == 'Feb':
                color_mn = 'magenta'
            elif mn in mnt30:
                color_mn = 'darkgoldenrod'
            else:
                color_mn = 'forestgreen'
                
            ax.annotate(mn, xy=(x,y), xycoords='data', 
                fontsize=12, fontweight='bold', color = color_mn)
            y -= 0.1
        x += 0.08
    
    # Draw borders
    y_mid = 0.76
    for i in range(7):
        if i == 0:
            plt.plot([-0.02,0.92],[y_mid, y_mid], color = 'black', linewidth=3)  # mid_horizontal
        else:
            plt.plot([-0.02,0.92],[y_mid, y_mid], color = 'darkgray', linewidth=1)  # mid_horizontal
        y_mid -= 0.1
        
    plt.plot([0.045, 0.045],[0.055,0.76], color = 'darkgray')  # left
    plt.plot([0.11, 0.11],[0.055,0.76], color = 'darkgray')  # left
    plt.plot([0.17, 0.17],[0.055,0.76], color = 'darkgray')  # left
    plt.plot([0.23, 0.23],[0.055,0.76], color = 'darkgray')  # left
    
    plt.plot([0.33,0.92],[0.86, 0.86], color = 'darkgray', linewidth=1)  # top_horizontal
    plt.plot([0.33,0.92],[0.96, 0.96], color = 'darkgray', linewidth=1)  # top_horizontal
    
    # outer borders
    plt.plot([-0.02,-0.02],[0.055,1.07], color = 'black', linewidth=4)  # left
    plt.plot([-0.018,-0.018],[0.055,1.07], color = 'black', linewidth=4)  # left
    plt.plot([-0.02,0.92],[0.055,0.055], color = 'black', linewidth=4)  # bottom
    plt.plot([-0.02,0.92],[1.07,1.07], color = 'black', linewidth=4)  # top
    plt.plot([0.92,0.92],[0.055,1.07], color = 'black', linewidth=4)  # right
    plt.plot([0.33,0.33],[0.055,1.07], color = 'black', linewidth=3)  # mid_vertical

    x_mid = 0.35 + 0.08
    for i in range(6):
        plt.plot([x_mid,x_mid],[0.055,1.07], color = 'darkgray', linewidth=1)  # mid_vertical
        x_mid += 0.08
    
    plt.xlim([-0.02,1])
    plt.ylim([0,1.1])
    
    plt.axis('off')
    
    return plt
    
if __name__ == '__main__':
    
    start_year = int(input('Enter the start year: '))
    end_year = int(input('Enter the end year: '))
    imagelist = []
    
    # Run algorithm for range of years
    for year in range(start_year, end_year + 1):
        months = fill_month(year)
        plt_obj = generate_calendar(months, year)
        
        buf = io.BytesIO()
        plt_obj.savefig(buf, format='png')
    
        buf.seek(0)
        im = Image.open(buf)
        imagelist.append(im.convert('RGB'))
        buf.close()
        plt_obj.close('all')  # uncomment if you want figures to pop up

    # Save pdf
    imagelist[0].save(r'Output//All_calendars_{}_till_{}.pdf'.format(start_year, end_year), save_all=True, append_images=imagelist[1:])
    