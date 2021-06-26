"""imports"""
from datetime import date
from datetime import datetime
import json
from configparser import ConfigParser
import sys
import logging
import mysql.connector
import josn



# pylint: disable=too-many-instance-attributes
class Details:
    """Details class"""

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birth = None
        self.gender = None
        self.nation = None
        self.city = None
        self.pin = None
        self.state = None
        self.qualification = None
        self.salary = None
        self.pan = None

    def data_validate(self):
        """Age Conversion"""
        self.birth = input("Enter the data of birth: ")
        born_data = self.birth
        age_result = ''
        formate = "%Y-%m-%d"
        try:
            datetime.strptime(self.birth, formate)
            born = datetime.strptime(born_data, formate).date()
            today = date.today()
            age_result = today.year \
                         - born.year - ((today.month, today.day) < (born.month, born.day))
            print(age_result)

        # pylint: disable=bare-except
        except:
            age_result = "Format should be %Y-%m-%d"
            print(age_result)
        else:
            print("D")

        return age_result

    def get_name(self):
        """Get name"""
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        return self.first_name, self.last_name

    def get_nationality(self):
        """Get Nationality"""
        self.nation = input("Enter the nationality: ")
        national_data = self.nation.capitalize()
        list1 = ["Indian", "American"]
        str1 = []
        if national_data in list1:
            str1.append(national_data)
        else:
            str1.append("Enter valid nationality")

        print(str1[0])
        return str1[0]

    def gender_data(self):
        """Gender Details"""
        self.gender = input("Enter the gender ")
        gender = self.gender.lower()
        gender = gender.capitalize()
        gender_list = []
        # pylint: disable=consider-using-in
        if gender == 'Male' or gender == 'Female':
            gender_list.append(gender)
        gender_list = gender_list.append("Not a Valid") if gender_list == [] else gender_list
        return gender_list[0]

    def get_city(self):
        """Get City"""
        self.city = input("Enter the city: ")
        city = self.city.lower()
        city = city.capitalize()
        return city


class AdditionalDetails(Details):
    """Additional Details"""

    # pylint: disable=useless-super-delegation
    def __init__(self):
        super().__init__()

    def get_pin(self):
        """Get Pin"""
        self.pin = int(input("Enter the code: "))
        return self.pin

    def get_state(self):
        """get State"""
        state_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam",
                      "Bihar", "Chhattisgarh", "Karnataka",
                      "Madhya Pradesh", "Odisha", "Tamil Nadu",
                      "Telangana", "West Bengal"]
        self.state = input("Enter the state ")
        state_data = []
        if self.state in state_list:
            state_data.append(self.state)
        else:
            state_data.append("State not present")
        return state_data[0]

    def get_qualification(self):
        """Get Qualification"""
        self.qualification = input("Enter the Qualification: ")
        return self.qualification

    @staticmethod
    def get_config():
        """config"""
        file_data = 'config.ini'
        config_res = ConfigParser()
        config_res.read(file_data)
        host_data = config_res['database']['host']
        user_data = config_res['database']['user']
        pass_data = config_res['database']['passwd']
        database_data = config_res['database']['database']

        return host_data, user_data, \
               pass_data, database_data


    def get_salary(self):
        """Get Salary"""
        self.salary = int(input("Enter the Salary "))
        salary_list = []
        # pylint: disable=chained-comparison
        if ((self.salary > 10000)
                and (self.salary < 90000)):
            salary_list.append(self.salary)

        else:
            salary_list.append("Salary from 11,000 to 89,000")
        return salary_list[0]

    def pan_number(self):
        """Get Pan"""
        self.pan = input('Enter the pan number: ')
        return self.pan

    @staticmethod
    def validate_date(birth, gender):
        """Get Validate"""
        gender_list = []
        # age_list = []
        birth_type = isinstance(birth, int)
        if birth_type:
            dob = birth
            gender_data = gender
            if ((gender_data == 'Male' and dob > 21) or
                    (gender_data == 'Female' and dob > 18)):
                gender_list.append("Success")

            else:
                gender_list.append("Invalid Input for DOB")

        gender_list.append("Format should be %Y-%m-%d")
        return gender_list[0]


    @staticmethod
    def create_table():
        """Create Table"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        status_data = []

        try:
            mycursor.execute(
                "CREATE TABLE first (First_name VARCHAR(50), last_name VARCHAR(50),"
                "age VARCHAR(100), Gender VARCHAR(100), National VARCHAR(50), "
                "City VARCHAR(50), State VARCHAR(50), Pin int UNSIGNED, Qualification VARCHAR(100),"
                " Salary VARCHAR(100), Pan VARCHAR(50), dateTime VARCHAR(50), "
                "id int PRIMARY KEY AUTO_INCREMENT)")

        # pylint: disable=bare-except
        except:
            status_data.append("Table Already Exists")
            print(status_data)

        return status_data

    @staticmethod
    def describe_table():
        """Describe Table"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        mycursor.execute("Describe first")
        for des_data in mycursor:
            print(des_data)

    # pylint: disable=too-many-arguments
    @staticmethod
    # pylint: disable=too-many-locals
    def insert_data(first_name, last_name, birth,
                    gender, nation, city, pin,
                    state, qualification, salary, pan):
        """Insert Data"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        date_time = datetime.now()
        mycursor.execute(
            "INSERT INTO first (First_name, last_name, age, "
            "Gender, National, City, State, "
            "Pin, Qualification, Salary, "
            "Pan, dateTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                first_name, last_name, birth,
                gender, nation, city,
                state, pin, qualification,
                salary, pan, date_time
            ))
        data_base.commit()
        return "Successfully Inserted"

    @staticmethod
    def view_table():
        """View Table"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        mycursor.execute("SELECT * FROM second")
        for table_data in mycursor:
            print(table_data)

    @staticmethod
    # pylint: disable=too-many-locals
    def validate_pan(pan_num):
        """validate Pan"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        mycursor.execute("SELECT Pan,dateTime FROM first")
        dates = []
        validate_result = []
        for x_data, y_data in mycursor:
            if pan_num == x_data:
                str1 = ''.join(y_data)
                str1 = str1.split()
                dates.append(str1)

        if len(dates) > 0:
            dates.reverse()
            date_formate = '%Y-%m-%d'
            get_date = date.today()
            d1_data = get_date.strftime(date_formate)
            print(d1_data)
            a_data = datetime.strptime(d1_data, date_formate)
            b_data = datetime.strptime(dates[0][0], date_formate)
            delta = a_data - b_data
            delta = abs(delta)

            # pylint: disable=expression-not-assigned
            validate_result.append("Activity in last five days") \
                if delta.days <= 5 else validate_result.append("Validate Success")

            print(validate_result)

        else:
            validate_result.append("New User")
        # return validate_result[0]


class ValidateJson(AdditionalDetails):
    """validation"""

    # pylint: disable=too-many-return-statements
    @staticmethod
    # pylint: disable=too-many-arguments
    def validate_all_data(birth, date_validate,
                          pan_activity, state,
                          salary, nation):
        """validate result"""
        count_validate = 0

        json_data = json.loads(josn.python_string)
        if birth != "Format should be %Y-%m-%d":
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['DReason'])
            return json_data['InvalidResponse'], json_data['DReason']
        # pylint: disable=consider-using-in
        if date_validate == "Success" or date_validate == 'Format should be %Y-%m-%d':
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['DReason'])
            return json_data['AResponse'], json_data['AReason']
        # pylint: disable=consider-using-in
        if pan_activity == "Validate Success" or pan_activity == "New User":
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
            return json_data['AResponse'], json_data['PanReason']

        if state != "State not present":
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
            return json_data['AResponse'], json_data['StateError']

        if salary != "Salary from 11,000 to 89,000":
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
            return json_data['AResponse'], json_data['Salary']

        if nation != "Enter valid nationality":
            count_validate += 1

        else:
            # ValidateJson().insert_new_data(json_data['InvalidResponse'], json_data['PanReason'])
            return json_data['AResponse'], json_data['Nation']

        return count_validate, "Success"

    @staticmethod
    def create_new_table():
        """Create new table"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        try:
            mycursor.execute(
                "CREATE TABLE second ("
                "Response_data VARCHAR(100), Reason VARCHAR(50),"
                "date_time VARCHAR(50) ,userId int PRIMARY KEY, "
                "FOREIGN KEY(userId) REFERENCES first(id))")
        # pylint: disable=bare-except
        except:
            print("Table Already Exists")

    @staticmethod
    def json_result(id_data):
        """Display Json Result"""
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        mycursor.execute("SELECT * FROM second")
        for table_data in mycursor:
            if id_data == table_data[3]:
                result_data = {
                    "RequestId": [table_data[3]],
                    "Response": [table_data[0]],
                    "Reason": [table_data[1]]
                }
                file_data = 'config.ini'
                config_data = ConfigParser()
                config_data.read(file_data)
                log_name = config_data['logging name']['name1']
                print(type(log_name))
                logging.basicConfig(filename=log_name, level=logging.DEBUG)
                logging.critical(result_data)
                print(json.dumps(result_data))

    @staticmethod
    def insert_new_data(validate, response, pan_data):
        """Insert into new table"""
        # pylint: disable=too-many-locals
        host_data, user_data, pass_data, database_data = AdditionalDetails.get_config()
        data_base = mysql.connector.connect(host=host_data, user=user_data,
                                            passwd=pass_data, database=database_data, use_pure=True)
        data_base2 = mysql.connector.connect(host=host_data, user=user_data,
                                             passwd=pass_data,
                                             database=database_data, use_pure=True)
        # data_base3 = mysql.connector.connect(host=host_data, user=user_data,
        #                                      passwd=pass_data,
        #                                      database=database_data, use_pure=True)
        mycursor = data_base.cursor()
        mycursor2 = data_base2.cursor()

        duplicate_id = 0

        time = datetime.now()
        mycursor.execute("SELECT Pan,id FROM first")
        mycursor2.execute("SELECT userId FROM second")
        for x_data, y_data in mycursor:
            if x_data == pan_data:
                a_data = y_data

        if duplicate_id == 0:
            mycursor.execute(
                "INSERT INTO second (Response_data, Reason, "
                "date_time,userId) VALUES (%s,%s,%s,%s)",
                (
                    validate, response, time, a_data
                ))
            data_base.commit()
            ValidateJson.json_result(a_data)


while True:
    DETAILS = AdditionalDetails()
    VALIDATES = ValidateJson()
    print("1.Enter the Details")
    print("2.Create Table -1")
    print("3.Insert Data into Database")
    print("4.Describe Table")
    print("5. View Table")
    print("6. Stop")
    print("7. Create Table -2")
    NUM = int(input("Enter the number: "))

    if NUM == 1:
        FIRST_NAME, LAST_NAME = DETAILS.get_name()
        BIRTH = DETAILS.data_validate()
        GENDER = DETAILS.gender_data()
        NATIONAL = DETAILS.get_nationality()
        CITY = DETAILS.get_city()
        PIN = DETAILS.get_pin()
        STATE = DETAILS.get_state()
        QUALIFICATION = DETAILS.get_qualification()
        SALARY = DETAILS.get_salary()
        NUMS = DETAILS.pan_number()
        VALIDATE = DETAILS.validate_date(BIRTH, GENDER)
        print(VALIDATE)
        PAN_VALIDATE = DETAILS.validate_pan(NUMS)

        print(FIRST_NAME, LAST_NAME, BIRTH,
              GENDER, NATIONAL, CITY,
              PIN, STATE, QUALIFICATION,
              SALARY, NUMS, VALIDATE, PAN_VALIDATE)

    elif NUM == 2:
        VALIDATES.create_table()

    elif NUM == 4:
        AdditionalDetails().describe_table()

    elif NUM == 5:
        AdditionalDetails().view_table()

    elif NUM == 3:
        RESULT, RESPONSE = VALIDATES.validate_all_data(BIRTH, VALIDATE,
                                                       PAN_VALIDATE, STATE,
                                                       SALARY, NATIONAL)
        print(RESULT)

        OUTPUT = isinstance(RESULT, int)

        if OUTPUT:
            AdditionalDetails().insert_data(
                FIRST_NAME, LAST_NAME, BIRTH,
                GENDER, NATIONAL, CITY, PIN,
                STATE, QUALIFICATION, SALARY, NUMS)

            ValidateJson.insert_new_data("Success", RESPONSE, NUMS)

        else:
            AdditionalDetails().insert_data(
                FIRST_NAME, LAST_NAME,
                BIRTH, GENDER, NATIONAL,
                CITY, PIN, STATE,
                QUALIFICATION,
                SALARY, NUMS)
            # pylint: disable=too-many-function-args
            ValidateJson.insert_new_data(RESULT, RESPONSE, NUMS)
    elif NUM == 6:
        sys.exit()

    elif NUM == 7:
        ValidateJson.create_new_table()
