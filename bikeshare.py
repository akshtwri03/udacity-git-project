import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago','new york city','washington']
    months = ['all','january','febraury','march','april','may','june']
    week = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    #Get user input for city (chicago, new york city, washington).
    city = ''
    while True:
        city = input("Please choose city either 'Chicago', 'New York City' or 'Washington': ").lower()
        if city.lower() not in cities:
            print("Sorry, wrong input. Please choose city either 'Chicago', 'New York City' or 'Washington'.")
            continue 
        else:
             break

    #Get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        month = input("Please choose 'all', or any month between january to june: ").lower()
        if month.lower() not in months:
            print("Sorry wrong input. Please choose 'all', or any month between 'January to June'.")
            continue
        else:
            break



    #Get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while True:
        day = input("Please choose 'all', or any day of a week: ").lower()
        if day.lower() not in week:
            print("Sorry wrong input. Please choose 'all', or any day of a week: ")
            continue
        else:
            break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load csv files into a data frame
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract time, month and day of week from Start Time to create new columns 
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # Filter by month if applicable
    if month != 'all':
        
        # Use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        # Filter by month to create the new dataframe
        df = df[df['month']==month]
        
    # Filter by date if applicable
    if day !='all':
        
        # Filter by day of week to create the new dataframe
        df = df[df['day']==day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Find and Display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('This is the most common month: ',common_month)
    
    # Find and Display the most common day of week
    common_day = df['day'].value_counts().idxmax()
    print('This is the most common day of week: ',common_day)

    # Find and Display the most common start hour
    popular_hour = df['hour'].mode().loc[0]
    print('The Most Popular Start Hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find and Display most commonly used start station
    start_station = df['Start Station'].mode().loc[0]
    print('The Most Common Start Station Is : ', start_station)
    
    # Find and Display most commonly used end station
    end_station=df['End Station'].mode().loc[0]
    print('The Most Common End Station Is : ', end_station)

    # Find and Display most frequent combination of start station and end station trip
    df['frequent'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_combination = df['frequent'].mode().loc[0]
    print('The most frequent combination of start station and end station trip: ',most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Find and Display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time: ',total_travel)

    # Find and Display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time',mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        
      # Find counts of user types
        user_count = df['User Type'].value_counts()
        

        # Find counts of gender
        gender_count = df['Gender'].value_counts()
        
    
        # Find earliest year of birth
        earliest_birth = df['Birth Year'].min()
       
    
        # Find most recent year of birth
        most_recent_birth = df['Birth Year'].max()
        
    
        # Find most common year of birth
        common_birth = df['Birth Year'].value_counts().idxmax()
        
        print('The most common birth year: ',common_birth)
    
    except:
        # Display error statement for gender column
        print('Gender column not available')
       
        # Display error for birth year column
        print('Birth Year column not available')
        
    else:
        
        # Display user counts
        print('The user types counts: ',user_count)
        
        # Display gender counts
        print('The gender counts are: ',gender_count)
    
        # Display earliest birth of year
        print('The most earliest birth year: ',earliest_birth)    

        # Display most recent birth year
        print('The most recent birth year: ',most_recent_birth)
        
        # Display most common birth year
        print('The most common birth year: ',common_birth)
    
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def more_raw_data(df):
    """ Accesses csv files and displays more rows of its raw data"""
 
 
    more_raw_data = ''
    i = 0
    while True:
        more_raw_data = input(" Would you like to see more records of raw biking data(yes/no):   ").lower()
        if more_raw_data == "yes":
            print(df.iloc[i:i+5])
            i+=5
            continue
        else:
            break
 
    print('-'*40)          
 
          
 
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_raw_data(df)
       
 
        """ Asks user to restart program and clears screen if yes """
 
        restart = input("Would you like to restart?  'Yes or No' ")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
