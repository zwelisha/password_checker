import pytest
from PasswordChecker import PasswordChecker
checker = PasswordChecker()
print(checker.met_conditions)
def test_password_is_valid():
    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("dgwewd@2019yes")
    assert str(error.value) == "password should have at least one uppercase letter"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("dg2L0*%@")
    assert str(error.value) == "password should be longer than than 8 characters"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("DGHEW20*%@")
    assert str(error.value) == "password should have at least one lowercase letter"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("12d")
    assert str(error.value) == "password should be longer than than 8 characters"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("GwerrfdDdjd")
    assert str(error.value) == "password should at least have one digit"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("Gwerrwedewd9")
    assert str(error.value) == "password should have at least one special character"

    with pytest.raises(Exception) as error:
        assert checker.password_is_valid("")
    assert str(error.value) == "password should exist"
    
