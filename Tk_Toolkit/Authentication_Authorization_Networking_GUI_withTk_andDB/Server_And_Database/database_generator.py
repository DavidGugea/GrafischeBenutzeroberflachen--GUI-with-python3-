import sqlite3 
import random 
import os

class DBGenerator():
    def __init__(self):
        # Get the wanted length of the password & UEC length from the user and store them 
        while True:
            self.password_length = input("How long do you want your passwords do be ? -- > ")

            try:
                self.password_length = int(self.password_length)
                if self.password_length <= 0:
                    raise
                break
            except:
                self.errorMessage("Your passwords length must be an integer and greater than 0")
                continue 
        while True:
            self.UEC_length = input("How long do you want your UEC codes to be ? -- > ")

            try:
                self.UEC_length = int(self.UEC_length)
                if self.UEC_length <= 0:
                    raise 
                break 
            except:
                self.errorMessage("Your UEC codes length must be an integer and greater than 0")
                continue

        # Delete the DB so that we can have again 100 workers, 50 administrators and one single owner.
        os.system("rm users_database.db")

        # Create the connection & cursor with the database
        self.connection = sqlite3.connect("users_database.db")
        self.cursor = self.connection.cursor()
        
        # Create the table with users data
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users_table(Username TEXT, Password TEXT, UEC TEXT, FirstName TEXT, SecondName TEXT, StreetNameStreetNumber TEXT, PostalCode NUMBER, CityName TEXT, Salary NUMBER, UserType TEXT)")
        self.connection.commit()

    def generate(self):
        # Create a list with lower-case, upper-case alphabet letters & with all the numbers from 1 to 9 (incl.) for the password & UEC code and another list that contains all of them ( lowercase, uppercase & digits )
        lower_case_letters = [chr(i) for i in list(range(ord("a"), ord("z") + 1, 1))]
        upper_case_letters = [chr(i) for i in list(range(ord("A"), ord("Z") + 1, 1))]
        digits = list(range(1, 10))
        all_sequences = list()
        all_sequences.extend(lower_case_letters)
        all_sequences.extend(upper_case_letters)
        all_sequences.extend(digits)

        # 100 workers, 50 administrators & 1 owner
        for user_number in range(1, 154):
            # Create all the data needed for the user
            Username = "Username{0}".format(user_number) 

            Password = str()
            for i in range(self.password_length):
                Password += str(random.choice(all_sequences))

            UEC = str()
            for i in range(self.UEC_length):
                UEC += str(random.choice(all_sequences))

            FirstName = "FirstName{0}".format(user_number)
            LastName = "SecondName{0}".format(user_number)

            StreetNameStreetNumber = "StreetName{0} {1}".format(user_number, random.choice(digits))

            PostalCode = random.randint(10000, 99999)
            CityName = "CityName{0}".format(user_number)

            Salary = 0
            UserType = str()
           
            if user_number <= 101: 
                # Worker
                Salary = random.randint(1000, 3000)
                UserType = "Worker"
            elif user_number in list(range(102, 153)):
                # Administrator
                Salary = random.randint(3000, 8000)
                UserType = "Administrator" 
            elif user_number == 153:
                # Owner
                Salary = random.randint(8000, 10000)
                UserType = "Owner"

            # Build a tuple with all the user-data and a string with the needed sql-query. We will use a secure way to enter values inside the database. ( Learned this from my book )
            query = "INSERT INTO users_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = ( Username, Password, UEC, FirstName, LastName, StreetNameStreetNumber, PostalCode, CityName, Salary, UserType)

            self.cursor.execute(query, values)
        
        # Save the entered users
        self.connection.commit()
        
        # Close the cursor & the connection with the database
        self.cursor.close()
        self.connection.close()

    def errorMessage(self, message):
        for i in range(3):
            print()
            
        print(message)
        print("Try again.")

        for i in range(3):
            print()

generator = DBGenerator()
generator.generate()