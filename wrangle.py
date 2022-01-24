# importing modules and other tools necessary for analaysis"
import pandas as pd
import env
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')



    
def get_happy():
    """This function reads in the world happiness dataset, writes data to a csv 
    file if a local file does not exist, and returns a df"""
    if os.path.isfile('zillow_df.csv'):
    # If csv file exists, read in data from csv file.\n",
        df = pd.read_csv('world-happiness-report-2021.csv', index_col = 0)
    else:
    # Read fresh data from db into a DataFrame.
        df = get_happy()
    # Write DataFrame to a csv file.
        df.to_csv('world-happiness-report-2021.csv')
    return df


def nulls_by_col(df):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_missing = num_missing / rows
    cols_missing = pd.DataFrame({'number_missing_rows': num_missing, 'percent_rows_missing': pct_missing})
    return cols_missing


def handle_missing_values(df, prop_required_column = .5, prop_required_row = .70):
	#function that will drop rows or columns based on the percent of values that are missing:\
	#handle_missing_values(df, prop_required_column, prop_required_row
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df


def remove_columns(df, cols_to_remove):  
	#remove columns not needed
    df = df.drop(columns=cols_to_remove)
    return df



def wrangle_happy():
    
    df = get_happy()
    
    # let's go ahead and drop the nulls
    df = df.dropna()
    df.isnull().sum()
    
    
    # upperwhisker can be dropped since this feature doesn't add to overall proj goal
    df.drop(columns = 'upperwhisker', inplace = True)

    
    # lowerwhisker can be dropped since this feature doesn't add to overall proj goal
    df.drop(columns = 'lowerwhisker', inplace = True)



    return df




def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames
    return train, validate, test DataFrames.
    '''
    train, test = train_test_split(wrangle_zillow, test_size = .2, random_state = 123)
    train, validate = train_test_split(train, test_size = .3, random_state = 123)
    
    return train, validate, test


def min_max_scaler(train, valid, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: mm_scaler, train_scaled_mm, test_scaled_mm
    This is a linear transformation. Values will lie between 0 and 1
    '''
    num_vars = list(train.select_dtypes('number').columns)
    scaler = MinMaxScaler(copy=True, feature_range=(0,1))
    train[num_vars] = scaler.fit_transform(train[num_vars])
    valid[num_vars] = scaler.transform(valid[num_vars])
    test[num_vars] = scaler.transform(test[num_vars])
    return scaler, train, valid, test

def outlier_function(df, cols, k):
	#function to detect and handle oulier using IQR rule
    for col in df[cols]:
        q1 = df.annual_income.quantile(0.25)
        q3 = df.annual_income.quantile(0.75)
        iqr = q3 - q1
        upper_bound =  q3 + k * iqr
        lower_bound =  q1 - k * iqr     
        df = df[(df[col] < upper_bound) & (df[col] > lower_bound)]
    return df