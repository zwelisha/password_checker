import pytest
from PasswordChecker import PasswordChecker
checker = PasswordChecker()
print(checker.met_conditions)

# Test if an exception is thrown for a password that has no uppercase.
def test_password_is_valid_uppercase():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("dgwewd@2019yes")
    assert str(error.value) == "password should have at least one uppercase letter"

# Test if an exception is thrown for passwords with less than or equal to 8 characters
def test_password_is_valid_eight_chars():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("dg2L0*%@")
    assert str(error.value) == "password should be longer than 8 characters"
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("12d")
    assert str(error.value) == "password should be longer than 8 characters"

# Test if an exception is thrown for passwords with  no lowercase
def test_password_is_valid_lowercase():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("DGHEW20*%@")
    assert str(error.value) == "password should have at least one lowercase letter"

# Test if an exception is thrown for password with no digit
def test_password_is_valid_digits():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("GwerrfdDdjd")
    assert str(error.value) == "password should at least have one digit"

# Test exception for the absence of special characters in password
def test_password_is_valid_special_characters():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("Gwerrwedewd9")
    assert str(error.value) == "password should have at least one special character"

# Test for password existence
def test_password_is_valid_exist():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("")
    assert str(error.value) == "password should exist"

# Tests for password_is_ok
def test_password_is_ok_exist():
    assert checker.password_is_ok("") == False
def test_password_is_ok_less_than_eight():
    assert checker.password_is_ok("qwe") == False
    assert checker.password_is_ok("qweB@123") == False
def test_password_is_ok_pass():
    assert checker.password_is_ok("qweB@123d") == True
