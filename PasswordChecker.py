import logging
import re
import time
"""
Written By : Zwelisha Mthethwa
Disclaimer: This code may be copied and used by anyone who finds it useful.
Date: 22 November 2019
"""
# create and configure logger
logging.basicConfig(filename = "logs/problems.log", level = logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger()
class PasswordChecker():
    """This class has several functions that perform different password validations"""
    # constructor for the password object
    def __init__(self):
        self._met_conditions = 0
    # function to get met_conditions
    def get_met_conditions(self):
        return self._met_conditions
    # function to set met conditions
    def set_met_conditions(self, value):
        self._met_conditions = value
    met_conditions = property(get_met_conditions, set_met_conditions)

    def password_is_valid(self, password):
        """
        Validates the string  password based on whether the following conditions are met.
        In addition the function throws relevant error messages if some of these conditions are not met
        Conditions:
            1. password should exist
            2. password should be longer than than 8 characters
            3. password should have at least one lowercase letter
            4. password should have at least one uppercase letter
            5. password should at least have one digit
            6. password should have at least one special character

        Parameters:
        password (str): the password argument passed

        Returns:
        None: Nothing, but raise an exception if one of the conditions fail.
        """
        conditions = 0
        try:
            if type(password) is str == False:
                logger.info("the function password_is_valid only accepts a string")
                raise Exception("the function password_is_valid only accepts a string")
            if len(password) == 0:
                raise Exception("password should exist")
            if len(password) > 8:
                conditions += 2 # start from 2 since the password exists and has more than 8 characters
                # check condition 5
                if re.search("[0-9]", password): # \d could be used instead of [0-9] to check condition 5
                    logger.info("Condition 5 passed")
                    conditions += 1
                else:
                    logger.info("password should at least have one digit")
                    raise Exception("password should at least have one digit")
                # check condition 3
                if re.search("[a-z]", password):
                    logger.info("Condition 3 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one lowercase letter")
                    raise Exception("password should have at least one lowercase letter")

                # check condition 4
                if re.search("[A-Z]", password):
                    logger.info("Condition 4 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one uppercase letter")
                    raise Exception("password should have at least one uppercase letter")
                # checking condition 6
                special_chars_compilation = re.compile("[@_!#$%^&*()<>?/\|}{~:\"']")
                if special_chars_compilation.search(password) != None:
                    logger.info("Condition 6 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one special character")
                    raise Exception("password should have at least one special character")
            else:
                logger.info("password should be longer than than 8 characters")
                raise Exception("password should be longer than 8 characters")
        except TypeError as e:
            logger.info(e)
        finally:
            PasswordChecker.set_met_conditions(self,conditions)
            logger.info("Conditions passed while executing password_is_valid function: " + str(conditions))
    def password_is_ok(self,password):
        conditions = 0
        if len(password) <= 8:
            return False
        else:
            conditions += 2 # start from 2 since the password exists and has more than 8 characters
            # check condition 5
            if re.search("[0-9]", password): # \d could be used instead of [0-9] to check condition 5
                logger.info("Condition 5 passed")
                conditions += 1
            # check condition 3
            if re.search("[a-z]", password):
                logger.info("Condition 3 passed")
                conditions += 1

            # check condition 4
            if re.search("[A-Z]", password):
                logger.info("Condition 4 passed")
                conditions += 1
            # checking condition 6
            special_chars_compilation = re.compile("[@_!#$%^&*()<>?/\|}{~:\"']")
            if special_chars_compilation.search(password) != None:
                logger.info("Condition 6 passed")
                conditions += 1
        return conditions >= 3
