
# coding: utf-8

# In[1]:


# Loading neccesary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# In[65]:


def Graphs0(dataframe):
    """
    Creates histogram and boxplot for all numeric columns in dataframeframe
    
    Used for creating histogram and boxplot of all the columns having numeric data type in the dataframe frame
    Saves the graphs with unique column names in the current working directory
    Version-0
    
    Parameters
    -----------
    dataframe: DataFrame
            DataFrame for which the graphs are to be plotted
    Returns
    ----------
    None
        
    """
    #cols=dataframe.columns # Getting all the columns names present in the dataframeset
    for col in dataframe.columns: # using for loop to loop through each column
        if ((dataframe[col].dtype==np.float64) or (dataframe[col].dtype==np.int64)): #Checking the dataframe type of each column
            dataframe[col].hist() #creating histogram for each column using hist() function
            plt.xlabel(col) # setting the name for x-axis of the histogram-- using the column name
            plt.ylabel("Frequency") # setting the name for y-axis of the histogram-- Frequency is used
            title_hist="Histogram of "+col # Creating unique name for each histogram by combining two strings string1:"Histogram" string2: it is the name of the column and is unique for each column
            plt.title(title_hist) # setting the name for the histogram
            #plt.show()  # The function Graphs() can also be used to display the histogram
            fname_hist="Histogram_"+col # Creating unique file name for each histogram by combining two strings string1:"Histogram_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_hist) #saving the histogram using the unique file name
            plt.close()
            
            
            dataframe.boxplot(column=col) #creating boxplot for each column using boxplot() function
            title_box="BoxPlot of "+col #Creating unique name for each boxplot by combining two strings string1:"BoxPlot" string2: it is the name of the column and is unique for each column
            plt.title(title_box) # setting the name for the boxplot
            fname_box="BoxPlot_"+col  # Creating unique file name for each boxplot by combining two strings string1:"Boxplot_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_box)#saving the boxplot using the unique file name
            #plt.show() # The function Graphs() can also be used to display the boxplot
            plt.close()
            


# In[50]:


def Graphs1_2(dataframe,col_number=[]):
    """
    Creates histogram and boxplot for numeric column specified by user (col_number) in dataframeframe
    
    Used for creating histogram and boxplot of  the columns having numeric data type in the dataframe 
    Takes two arguments, 2nd argument is a optional argument if the user does not specify the column number the function create graphs for all the numeric columns
    Saves the graphs with unique column names in the current working directory
    Version-1,2
    
    Parameters
    -----------
    dataframe: DataFrame
            DataFrame for which the graphs are to be plotted
    col_number: List
            List of columns numbers for which 
    Returns
    ----------
    None
        
    """
    if not col_number: #check if the argument is passed or not
        no_col=dataframe.shape[1] #stores numner of columns in the data frame into no_col variable
        col_number=list(range(0,no_col)) #creating a list of number of columns
    for i in col_number: 
        col=dataframe.columns[i] #storing the name of column into col variable
        if ((dataframe[col].dtype==np.float64) or (dataframe[col].dtype==np.int64)): #Checking the dataframe type of each column
            dataframe[col].hist() #creating histogram for each column using hist() function
            plt.xlabel(col) # setting the name for x-axis of the histogram-- using the column name
            plt.ylabel("Frequency") # setting the name for y-axis of the histogram-- Frequency is used
            title_hist="Histogram of "+col # Creating unique name for each histogram by combining two strings string1:"Histogram" string2: it is the name of the column and is unique for each column
            plt.title(title_hist) # setting the name for the histogram
            #plt.show()  # The function Graphs() can also be used to display the histogram
            fname_hist="Histogram_"+col # Creating unique file name for each histogram by combining two strings string1:"Histogram_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_hist) #saving the histogram using the unique file name
            plt.close()
           
        
            dataframe.boxplot(column=col) #creating boxplot for each column using boxplot() function
            title_box="BoxPlot of "+col #Creating unique name for each boxplot by combining two strings string1:"BoxPlot" string2: it is the name of the column and is unique for each column
            plt.title(title_box) # setting the name for the boxplot
            fname_box="BoxPlot_"+col  # Creating unique file name for each boxplot by combining two strings string1:"Boxplot_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_box)#saving the boxplot using the unique file name
            #plt.show() # The function Graphs() can also be used to display the boxplot
            plt.close()
        


# In[51]:


def Graphs3(dataframe,col_number=[]):
    """
    Creates histogram, boxplot and bar chart for columns specified by user (col_number) in dataframeframe
    
    Used for creating histogram,boxplot,barchart of  the columns having numeric data type in the dataframe 
    Takes two arguments, 2nd argument is a optional argument if the user does not specify the column number the function create graphs for all the numeric columns
    Saves the graphs with unique column names in the current working directory
    Version-3
    
    Parameters
    -----------
    dataframe: DataFrame
            DataFrame for which the graphs are to be plotted
    col_number: List
            List of columns numbers for which 
    Returns
    ----------
    None
        
    """
    
    if not col_number: #check if the argument is passed or not
        no_col=dataframe.shape[1] #stores numner of columns in the data frame into no_col variable
        col_number=list(range(0,no_col)) #creating a list of number of columns
    for i in col_number: 
        col=dataframe.columns[i] #storing the name of column into col variable
        if ((dataframe[col].dtype==np.float64) or (dataframe[col].dtype==np.int64)): #Checking the dataframe type of each column
            dataframe[col].hist() #creating histogram for each column using hist() function
            plt.xlabel(col) # setting the name for x-axis of the histogram-- using the column name
            plt.ylabel("Frequency") # setting the name for y-axis of the histogram-- Frequency is used
            title_hist="Histogram of "+col # Creating unique name for each histogram by combining two strings string1:"Histogram" string2: it is the name of the column and is unique for each column
            plt.title(title_hist) # setting the name for the histogram
            #plt.show()  # The function Graphs() can also be used to display the histogram
            fname_hist="Histogram_"+col # Creating unique file name for each histogram by combining two strings string1:"Histogram_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_hist) #saving the histogram using the unique file name
            plt.close()
            
            
            dataframe.boxplot(column=col) #creating boxplot for each column using boxplot() function
            title_box="BoxPlot of "+col #Creating unique name for each boxplot by combining two strings string1:"BoxPlot" string2: it is the name of the column and is unique for each column
            plt.title(title_box) # setting the name for the boxplot
            fname_box="BoxPlot_"+col  # Creating unique file name for each boxplot by combining two strings string1:"Boxplot_" string2: it is the name of the column and is unique for each column
            plt.savefig(fname_box)#saving the boxplot using the unique file name
            #plt.show() # The function Graphs() can also be used to display the boxplot
            plt.close()
        else:
            dataframe[col].value_counts().plot(kind='bar')
            plt.xlabel(col)
            plt.ylabel("Frequency")
            title_bar="Bar chart of "+col
            plt.title(title_bar)
            fname_bar="Barchart_"+col
            plt.savefig(fname_bar)
            #plt.show()
            plt.close()


# In[74]:


def Graphs4(dataframe,col_number=[],directory=None):
    """
    Creates histogram, boxplot and bar chart for columns specified by user (col_number) in the directory mentioned by the user
    
    Used for creating histogram,boxplot,barchart of  the columns having numeric data type in the dataframe 
    Takes two arguments, 2nd argument is a optional argument if the user does not specify the column number the function create graphs for all the numeric columns
    By default Saves the graphs with unique column names in the current working directory else it saves it the directory mentioned by the user.
    Version-4
    
    Parameters
    -----------
    dataframe: DataFrame
            DataFrame for which the graphs are to be plotted
    col_number: List
            List of columns numbers for which 
    Returns
    ----------
    None
        
    """
    if not col_number: #check if the argument is passed or not
        no_col=dataframe.shape[1] #stores numner of columns in the data frame into no_col variable
        col_number=list(range(0,no_col)) #creating a list of number of columns
    for i in col_number: 
        col=dataframe.columns[i] #storing the name of column into col variable
        if ((dataframe[col].dtype==np.float64) or (dataframe[col].dtype==np.int64)): #Checking the dataframe type of each column
            dataframe[col].hist() #creating histogram for each column using hist() function
            plt.xlabel(col) # setting the name for x-axis of the histogram-- using the column name
            plt.ylabel("Frequency") # setting the name for y-axis of the histogram-- Frequency is used
            title_hist="Histogram of "+col # Creating unique name for each histogram by combining two strings string1:"Histogram" string2: it is the name of the column and is unique for each column
            plt.title(title_hist) # setting the name for the histogram
            #plt.show()  # The function Graphs() can also be used to display the histogram
            fname_hist="Histogram_"+col # Creating unique file name for each histogram by combining two strings string1:"Histogram_" string2: it is the name of the column and is unique for each column
            
            plt.savefig(os.path.join(directory,fname_hist)) #saving the histogram using the unique file name
            plt.close()
            
            
            dataframe.boxplot(column=col) #creating boxplot for each column using boxplot() function
            title_box="BoxPlot of "+col #Creating unique name for each boxplot by combining two strings string1:"BoxPlot" string2: it is the name of the column and is unique for each column
            plt.title(title_box) # setting the name for the boxplot
            fname_box="BoxPlot_"+col  # Creating unique file name for each boxplot by combining two strings string1:"Boxplot_" string2: it is the name of the column and is unique for each column
            plt.savefig(os.path.join(directory,fname_hist))#saving the boxplot using the unique file name
            #plt.show() # The function Graphs() can also be used to display the boxplot
            plt.close()
        else:
            dataframe[col].value_counts().plot(kind='bar')
            plt.xlabel(col)
            plt.ylabel("Frequency")
            title_bar="Bar chart of "+col
            plt.title(title_bar)
            fname_bar="Barchart_"+col
            plt.savefig(os.path.join(directory,fname_bar))
            #plt.show()
            plt.close()


# In[2]:


data=pd.read_csv("C:\\Users\\Ramya Ramprakash\\Python Praxis\\Machine Learning\\cars.csv")
#Graphs0(data)
#Graphs1_2(data,[2,4])
#Graphs1_2(data)
#Graphs3(data)
#Graphs3(data,[0,5,8])
#Graphs4(data,col_number=[1],directory="C:\\Users\\Ramya Ramprakash\\Python Praxis\\Machine Learning")


#for col in data.columns[1:]:
    #print(col.dtypes)
#for col in data.columns:
    #print(data[col].dtype)
#data.hist(figsize=(15,15))--important
#plt.show()
#data['MPG'].hist()
#plt.show()

