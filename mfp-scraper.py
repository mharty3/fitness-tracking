import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def single_date_scrape(username, date):
    '''Returns a list of the total calories, grams of carbs, fat, and protein
    and macro percentages entered into a diary on the given date(YYYY-MM-DD)'''
    url_head = 'http://www.myfitnesspal.com/food/diary/'
    url = '%s/%s?date=%s' % (url_head, username, date)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    right_table = soup.find('tr', class_='total')  # find the table containing the daily totals

    calories = right_table.findAll('td')[1].string  # find the total calories
    macros_g = right_table.findAll('span', class_='macro-value')  # Find all macro values
    macros_pct = right_table.findAll('span', class_='macro-percentage')  # Find all macro percentages

    macros_g = [m.contents[0].strip() for m in macros_g]  # Get contents and strip the macro values
    macros_pct = [m.contents[0].strip() for m in macros_pct]  # Get contents and strip the macro percentages

    daily_values = []
    daily_values.append(date)
    daily_values.append(calories)
    daily_values.extend(macros_g)
    daily_values.extend(macros_pct)

    return daily_values

def date_range_scrape(username, start_date, end_date):
    dates = pd.date_range(start_date, end_date).strftime('%Y-%m-%d')
    data = []
    for date in dates:
        data.append(single_date_scrape(username, date))
    columns = ['Date', 'Calories', 'Carbs[g]', 'Fat[g]', 'Protein[g]', 'Carbs[%]',
                                                  'Fat[%]', 'Protein[%]']
    return pd.DataFrame(data, columns=columns).set_index('Date')

if __name__ == '__main__':
    username = input('What is your username?  ')
    start_date = input('Enter the first date. (YYYY-MM-DD)  ')
    end_date = input('Enter the last date. (YYYY-MM-DD)  ')
    out_path = input('Enter the path to the .csv file ')

    df = date_range_scrape(username, start_date, end_date)
    print(df)
    df.to_csv(out_path)




