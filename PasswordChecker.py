import logging
import re
import time
# create and configure logger
logging.basicConfig(filename = "logs/problems.log", level = logging.DEBUG)
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
        bool: True if the password is valid, otherwise False
        """
        conditions = 0
        try:
            if not password:
                logger.error("password should exist")
                return "password shoud exist"
            if len(password) == 0:
                raise Exception("The password should be longer than 8 characters")
            if len(password) > 8:
                conditions += 2 # start from 2 since the password exists and has more than 8 characters
                # check condition 3
                if re.search("[a-z]", password):
                    logger.info(time.time())
                    logger.info("Condition 3 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one lowercase letter")
                    raise Exception("password should have at least one lowercase letter")

                # check condition 4
                if re.search("[A-Z]", password):
                    logger.info(time.time())
                    logger.info("Condition 4 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one uppercase letter")
                    raise Exception("password should have at least one uppercase letter")

                # check condition 5
                if re.search("[0-9]", password): # \d could be used instead of [0-9] to check condition 5
                    logger.info(time.time())
                    logger.info("Condition 5 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one digit")
                    raise Exception("password should have at least one digit")

                # checking condition 6
                special_chars_compilation = re.compile("[@_!#$%^&*()<>?/\|}{~:\"']")
                if special_chars_compilation.search(password) != None:
                    logger.info(time.time())
                    logger.info("Condition 6 passed")
                    conditions += 1
                else:
                    logger.info("password should have at least one special character")
                    raise Exception("password should have at least one special character")
            else:
                logger.info("password should exist")
                raise Exception("password should exist")
        except TypeError as e:
            logger.log(e)
            return "password shoud be a string"
        finally:
            PasswordChecker.set_met_conditions(self,conditions)
            logger.info("Conditions passed " + str(conditions))
            return conditions == 6
def main():
    checker = PasswordChecker()
    print(checker.password_is_valid(""))

if __name__ == '__main__':
    main()
