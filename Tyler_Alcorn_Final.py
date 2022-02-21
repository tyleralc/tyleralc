import csv 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys 
import requests
from bs4 import BeautifulSoup
import matplotlib.dates
from datetime import datetime 
from matplotlib.dates import DateFormatter

def default_function():
    #default mode
    #add the functions/code you need to scrape all your data
    #print all the data you scrape/request but and if it's huge, show the dimensions and a sample

    #get the dataframe setup 
    races_df = pd.read_csv('races.csv')

    #set the index to the year 
    races_df_date = races_df.set_index('year').copy()

    # only get the italian GPs and sort 
    italy_df = races_df_date[races_df_date['name']=='Italian Grand Prix']

    #clean up the dataframe 
    italy_df1 = italy_df.drop(columns =['time', 'url']).sort_index()

    # API with iteration using years_and_rounds_order dict

    #dict creation
    years_and_rounds={}
    with open('races.csv', 'r') as csvfile:
        lines= csv.reader(csvfile, delimiter=',')
        for row in lines:
            if row[4] == "Italian Grand Prix":
                years_and_rounds[row[1]]=row[2]
            else:
                continue
    #sort the keys 
    years_and_rounds_order={}
    for key in sorted(years_and_rounds):
        years_and_rounds_order[key]=years_and_rounds[key]
    #end of dict creation 

    #API request for number of accidents 
    Accident_count=[]
    for key, val in years_and_rounds_order.items():
        url = "http://ergast.com/api/f1/"+ key + "/" + val +"/status"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        lines= response.text.split('\n')
        if response.text.find("Accident") == -1:
            Accident_count.append('0')
        else: 
            for line in lines:
                if "Accident" in line:
                    parts = line.split('"')
                    Accident_count.append(parts[3])

    #list creation 
    years_and_rounds={}
    with open('races.csv', 'r') as csvfile:
        lines= csv.reader(csvfile, delimiter=',')
        for row in lines:
            if row[4] == "Italian Grand Prix":
                years_and_rounds[row[1]]=row[2]
            else:
                continue
    #make a list of the years
    years_list=[]
    for key in sorted(years_and_rounds):
        years_list.append(key)
    #end of list creation

    #fastest lap list creation from web scraping 
    Italy_fastlap=[]
    for year in years_list:
        website = 'https://www.formula1.com/en/results.html/' +year+'/fastest-laps.html'
        content = requests.get(website)
        soup = BeautifulSoup(content.content, 'html.parser')
        table= soup.find('table', class_='resultsarchive-table')
        columns = table.find('thead').find_all('th')
        column_names= [c.string for c in columns]
        table_rows = table.find('tbody').find_all('tr')

        table_list = []
        for tr in table_rows:
            td = tr.find_all('td')
            row = [str(tr.get_text()).strip() for tr in td]
            table_list.append(row)
        # times_df= pd.DataFrame(l, columns=column_names)
        # times_df
        
        for lst in table_list:
            if 'Italy' in lst:
                Italy_fastlap.append(lst[4])      
    #output is each year write code to only take the 'Italy' row lap time     

    #add the accident count list and fastest lap list to the italy_df1
    italy_df1['Accident_Number']= Accident_count
    italy_df1['Fastest_Lap']= Italy_fastlap
    italy_df1['Fastest_Lap']= pd.to_datetime(italy_df1['Fastest_Lap'], format= '%M:%S.%f')
    italy_df1.reset_index(inplace=True)

    #create a csv file of the dataframe 
    italy_df1.to_csv('Italy_dataframe.csv')

    #create a visualization and statist test for speeds versus accident count 
    #make the figure
    fig, ax1 = plt.subplots()
    plt.rcParams['figure.figsize']=(12,6)
    #make the times useable for the graph to plot 
    x=italy_df1['year'].to_list()
    y= italy_df1['Accident_Number'].tolist()
    y2= italy_df1['Fastest_Lap'].tolist()

    #first plot
    accidents_plots= ax1.scatter(x, y, label= 'Number of Accidents', color='blue', s=20 )
    ax1.set_ylabel('Number of Accidents', color= 'blue')
    #x axis fix 
    every_nth = 10
    for n, label in enumerate(ax1.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False) 

    #making second y axis
    ax2= ax1.twinx()

    #second plot
    times_plot= ax2.plot(x, y2, color= 'orange', label='Fastest Lap')
    ax2.set_ylabel('Fastest Lap Time', color='orange' )
    #y axis fix for time
    ax2.yaxis.set_major_formatter(DateFormatter('%M:%S'))
    ax2.invert_yaxis()
    plt.savefig('Italy_graph.pdf')
    print('It worked!')

def static_function(path_to_static_data):
    #static mode
    #add the functions/code you need to open and print the static copies of your data
    #you can use the path provided in the command line argument to open the data

    with open('Italy_dataframe.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)


if __name__ == '__main__': #for your purpose, you can think of this line as the saying "run this chunk of code first"
    if len(sys.argv) == 1: # this is basically if you don't pass any additional arguments to the command line
        #default mode
        #print eveything or the dimensions and a sample 
        default_function()
        
    elif sys.argv[1] == '--static': # if you pass '--static' to the command line
        #static mode
        #print a sample of the static datasets you have built from your scraping
        path_to_static_data = sys.argv[2]
        static_function(path_to_static_data)