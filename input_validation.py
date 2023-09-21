import re  # regular Expressions

validSpecialCharacters = [
    '!', '#', '$', '%', '&', "'", '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~'
]


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """

    if(type(email) != str):
        return False
    if(not email or email == ""):
        return False
    splitAt = email.split('@')
    if(len(splitAt) != 2):
        return False
    if(len(splitAt[0]) == 0):
        return False
    firstChar = splitAt[0][0]
    if(not firstChar.isalnum() and firstChar != '"'):
        return False
    lastChar = splitAt[0][-1]
    if(not lastChar.isalnum() and lastChar != '"'):
        return False
    splitDot = splitAt[1].split('.')
    if(len(splitDot) < 2):
        return False

    for character in splitAt[0]:
        isAlnum = character.isalnum()
        isDot = character == '.'
        isSpecialAllowed = validSpecialCharacters.__contains__(character)
        valid = isAlnum or isDot or isSpecialAllowed
        if (not valid):
            return False

    # DOMAINS BEFORE DOT
    for character in splitDot[0]:
        isAlnum = character.isalnum()
        isDot = character == '.'
        isSpecialAllowed = validSpecialCharacters.__contains__(character)
        valid = isAlnum or isDot or isSpecialAllowed
        if (not valid):
            return False

    # AFTER DOT
    for character in splitDot[1:]:
        isAlpha = character.isalpha()
        isDot = character == '.'
        valid = isAlpha or isDot
        if (not valid):
            return False
    return True


def is_valid_password(password: str):
    if(type(password) != str): return ValueError
    length = len(password)
    if(length < 8): return False
    typesOfCharacters = get_types_of_characters_used(password)
    if(typesOfCharacters < 2): return False
    if(typesOfCharacters == 2 and length < 20): return False
    if(typesOfCharacters == 3 and length < 13): return False
    return True


def get_types_of_characters_used(password: str) -> int:
    types = {"isLower": False, "isUpper": False,
             "isDigit": False, "isSpecial": False}
    for character in password:
        if(character.isalpha() and character.isupper()): types["isUpper"] = True
        elif(character.isalpha() and character.islower()): types["isLower"] = True
        elif(character.isdigit()): types["isDigit"] = True
        else: types["isSpecial"] = True
    typeCount = sum(types.values())
    print(typeCount)
    return typeCount


print(is_valid_password("aB1aaaaaaaabb"))
