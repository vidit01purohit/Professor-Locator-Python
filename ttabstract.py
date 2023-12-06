import pandas as pd
from datetime import datetime

professors=["Dr. Akhtar Rasool","Dr. Manish Pandey","Dr. Jay Trilok Choudhary","Dr. Deepak Singh Tomar","Dr. Nilay Khare","Dr. Dhirendra Pratap Singh","Dr. Mitul Kumar Ahirwar","Dr. Rajesh Wadhwani","Dr. Pragati Agrawal","Dr. Minu Chawla","Dr. Saiyam Shukla","Dr. Vaibhav Soni","Dr. Vijay Bhaskar","Dr. Shweta Jain"]

professor_codes={"Dr. Akhtar Rasool": "AR",
                 "Dr. Manish Pandey": "MP",
                 "Dr. Jay Trilok Choudhary": "JTC",
                 "Dr. Deepak Singh Tomar": "DST",
                 "Dr. Nilay Khare": "NK",
                 "Dr. Dhirendra Pratap Singh": "DPS",
                 "Dr. Mitul Kumar Ahirwar": "MKA",
                 "Dr. Rajesh Wadhwani": "RW",
                 "Dr. Pragati Agrawal": "PA",
                 "Dr. Minu Chawla": "MC",
                 "Dr. Saiyam Shukla": "SS",
                 "Dr. Vaibhav Soni": "VS",
                 "Dr. Vijay Bhaskar": "VB",
                 "Dr. Shweta Jain": "SJ"}

class Ttabstract:
    def __init__(self, prof_name):
        self.prof_name = prof_name
        self.curr_time = ''
        self.curr_day = ''

    def gettimeday(self):
        period = datetime.today().strftime("%p")
        from_hour = datetime.today().hour
        to_hour = from_hour + 1
        if from_hour >= 13:
            from_hour = from_hour - 12
        if to_hour == 12:
            period = "PM"
        if to_hour >= 13:
            to_hour = to_hour - 12
        self.curr_time = f"{from_hour}:00 - {to_hour}:00 {period}"
        self.curr_day = datetime.today().strftime("%A").upper()[0:3]

    def getdetails(self):
        prof_code = professor_codes[self.prof_name]
        self.gettimeday()
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
            update = df.loc[self.curr_day, self.curr_time]
            print("BOT: " + update)
        except:
            print("BOT: Sorry, college time is over!")


