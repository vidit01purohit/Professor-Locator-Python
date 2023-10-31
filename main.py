import ttabstract
from thefuzz import fuzz, process
import pandas as pd
from datetime import datetime

period = datetime.today().strftime("%p")
from_hour = datetime.today().hour
to_hour = from_hour + 1
if from_hour >= 13:
    from_hour = from_hour - 12
if to_hour == 12:
    period = "PM"
if to_hour >= 13:
    to_hour = to_hour - 12
curr_time = f"{from_hour}:00 - {to_hour}:00 {period}"
curr_day = datetime.today().strftime("%A").upper()[0:3]
print(curr_time," ",curr_day)
# Professor name abstraction

def find_professors(profess, person):
    found_professors = []
    for professor in profess:
        percent_matched = fuzz.token_set_ratio(professor, person)
        if percent_matched > 60:
            found_professors.append(professor)
    return found_professors

professors = ttabstract.professors
search_is_on = True
while search_is_on:
    text = input("Search: ")
    found_professors = find_professors(professors, text)

    if len(found_professors) == 0:
        print("Not found!")

    else:
        # Abstracting Professor code
        prof_code = ttabstract.professor_codes[found_professors[0]]

        # Data Abstraction
        df = pd.read_excel('Department_name.xlsx', header=None, skiprows=5, skipfooter=1,
                           sheet_name=prof_code)
        # Extract the column names from the 7th row
        column_names = df.iloc[0]

        # Set the column names
        df.columns = column_names

        # Drop the first row (since it's now the column names)
        df = df.drop(0)

        # Set the first column as the index
        df.set_index(df.columns[0], inplace=True)

        try:
            update = df.loc[curr_day, curr_time]
            print(update)
        except:
            print("Sorry, college time is over!")

    ask_user = input("Do you want to search more? (Yes/No)").lower()
    if ask_user == "no":
        print("Thank you! for searching")
        search_is_on = False
