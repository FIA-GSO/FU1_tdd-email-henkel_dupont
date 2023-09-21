import pytest
from input_validation import is_valid_email

@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
,   ("email@example.com")
,   ("firstname.lastname@example.com")
,   ("email@subdomain.example.com")
,   ("firstname+lastname@example.com")
,   ("email@123.123.123.123")
,   ("email@[123.123.123.123]")
,   ('"email"@example.com')
,   ("1234567890@example.com")
,   ("email@example-one.com")
,   ("_______@example.com")
,   ("email@example.name")
,   ("email@example.museum")
,   ("email@example.co.jp")
,   ("firstname-lastname@example.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen
,   ("plainaddress")
,   ("#@%^%#$@#$@#.com")
,   ("@example.com")
,   ("Joe Smith <email@example.com>")
,   ("email.example.com")
,   ("email@example@example.com")
,   (".email@example.com")
,   ("email.@example.com")
,   ("email..email@example.com")
,   ("あいうえお@example.com")
,   ("email@example.com (Joe Smith)")
,   ("email@example")
,   ("email@-example.com")
,   ("email@example.web")
,   ("email@111.222.333.44444")
,   ("email@example..com")
,   ("Abc..123@example.com")
])
def test_is_valid_email__ungueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is False