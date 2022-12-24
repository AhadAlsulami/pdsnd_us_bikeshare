import time
import pandas as pd
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
    
    
    print('Welcome! 🚲︎\nLet\'s explore some US bikeshare data!\n\n')
    
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("First, Choose a city.\nit could be: Chicago, New York City or Washington:\n ").lower()
    
    while city not in CITY_DATA.keys():
        city = input("Wrong! Choose a city from the following: Chicago, New York City or Washington:\n ").lower()
        
    # get user input for month (all, january, february, ... , june)
    month = input("\nNow Choose a month from January to June (Or you can type All):\n ").lower()
    while month not in months:
        month = input("Invalid Input! Try again:\n ").lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nChoose a day of the week (Or you can type All):\n ").lower()
    while day not in days:
        day = input("Invalid Input! Try again:\n ").lower()
        
    print("\n",'-'*40,"\n")
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print("The most common month of travel: ", calendar.month_name[df['month'].value_counts().idxmax()])
    
    # display the most common day of week
    print("The most common day of travel: ", df['day_of_week'].value_counts().idxmax())
    
    # display the most common start hour
    print("The most common start hour of travel: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("\n",'-'*40, "\n")


     
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used Start Station: ", df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print("The most commonly used End Station: ", df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    combination = df['Start Station'] + " --to--> " + df['End Station']
    print("The most frequent combination of Start and End Stations: ", (combination).value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("\n",'-'*40, "\n")



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total of travel time: ", df['Trip Duration'].sum())

    # display mean travel time
    print("The Average of travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("\n",'-'*40, "\n")


    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Number of users:\n",df['User Type'].value_counts(),"\n")

    try:
        # Display counts of gender
        print('\nNumber of users based on gender:\n', df['Gender'].value_counts(),"\n")

        # Display earliest, most recent, and most common year of birth
        print("The oldest year of birth: ", int(df['Birth Year'].min()))
        print("The youngest year of birth: ", int(df['Birth Year'].max()))
        print("The most common year of birth:: ", int(df['Birth Year'].mode()))
        
    except:
        print("Sorry! There are no data about Gender and Birth in Washington.")
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("\n",'-'*40, "\n")


    
def raw_data(df):
    """Displays 5 lines of raw data each time upon request."""
    
    count = 0 
    while True:
        answer = input("\nWould you like to see a 5 lines of the data? Enter yes or no.\n ").lower()
        if answer == 'yes':
            print(df.iloc[count:count + 5])
            count += 5
        else:
            break
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n ')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()