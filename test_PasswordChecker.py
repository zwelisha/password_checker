from PasswordChecker import PasswordChecker
checker = PasswordChecker()
print(checker.met_conditions)
def test_password_is_valid():
    assert checker.password_is_valid("dgwewd@2019yes") == False
    assert checker.password_is_valid("dgwewd2L0*%@") == True
    assert checker.password_is_valid("dgwewd20*%@") == False
    assert checker.password_is_valid("") == False
    assert checker.password_is_valid(1234) == False
    assert checker.password_is_valid("") == False
    print(checker.password_is_valid("dgwewd@2019yes"))
