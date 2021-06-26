import unittest
import pytest
import details_mysql


class TestMain(unittest.TestCase):
    """main data operation"""

    @staticmethod
    def test_name():
        """get assert name"""
        first_name, last_name = details_mysql.AdditionalDetails().get_name()
        assert first_name, last_name != ''

    @staticmethod
    def test_age():
        """check assert dob"""

    age_of_person = details_mysql.AdditionalDetails().data_validate()
    assert age_of_person != "Formate should be %Y-%m-%d"

    @staticmethod
    def test_gender():
        """check assert gender"""
        check_gender = details_mysql.AdditionalDetails().gender_data()
        assert check_gender != 'Not a Valid'

    @staticmethod
    def test_nation():
        """check nationality"""
        check_nation = details_mysql.AdditionalDetails().get_nationality()
        assert check_nation != 'Enter valid nationality'

    @staticmethod
    def test_city():
        """check city"""
        check_city = details_mysql.AdditionalDetails().get_city()
        assert check_city != 'No blank details'

    @staticmethod
    def test_pin():
        """check pin-code"""
        check_pin_code = details_mysql.AdditionalDetails().get_pin()
        assert check_pin_code != 'Enter valid Pin'

    @staticmethod
    def test_state():
        """check state"""
        check_state_result = details_mysql.AdditionalDetails().get_state()
        assert check_state_result != 'State not present'

    @staticmethod
    def test_qualification():
        """check qualification"""
        check_qualification_result = details_mysql.AdditionalDetails().get_qualification()
        assert check_qualification_result != 'Qualification field not be empty'

    @staticmethod
    def test_salary():
        """check salary data"""
        check_salary = details_mysql.AdditionalDetails().get_salary()
        assert check_salary != 'Salary from 11,000 to 89,000'

    @staticmethod
    def test_pan():
        """check pan card"""
        check_pan_card = details_mysql.AdditionalDetails().pan_number()
        assert check_pan_card != 'Enter the PanCard'

    @staticmethod
    def test_validate():
        """check validate"""
        check_correct = details_mysql.AdditionalDetails().validate_date(
            details_mysql.AdditionalDetails().data_validate(), details_mysql.AdditionalDetails().gender_data())
        assert check_correct == 'Success'

    @staticmethod
    def test_table():
        """check table creation"""
        check_table = details_mysql.AdditionalDetails().create_table()
        assert check_table != "Table Already Exists"

    @staticmethod
    def test_insert():
        """check insert data"""
        check_data = details_mysql.AdditionalDetails().insert_data()
        assert check_data == 'Successfully Inserted'

    @staticmethod
    def test_pan():
        """check pan activity"""
        check_pan = details_mysql.AdditionalDetails().validate_pan(details_mysql.AdditionalDetails().pan_number())
        assert check_pan != "Activity in last five days"
