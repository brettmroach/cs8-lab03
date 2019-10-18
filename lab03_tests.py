# Student: Brett Roach 6907380
# CS8 (F19)

# lab03_tests.py

from lab03 import notStringContainingR

# Tests for notStringContainingR
def test_notStringContainingR_1():
    assert notStringContainingR("word") == False

def test_notStringContainingR_2():
    assert notStringContainingR("super") == False

def test_notStringContainingR_3():
    assert notStringContainingR("ReEl") == False

def test_notStringContainingR_4():
    assert notStringContainingR("") == True

def test_notStringContainingR_5():
    assert notStringContainingR(3.14) == True


from lab03 import hasVowel

# Tests for hasVowel
def test_hasVowel_1():
    assert hasVowel(True) == False

def test_hasVowel_2():
    assert hasVowel("Pythn") == False

def test_hasVowel_3():
    assert hasVowel("") == False

def test_hasVowel_4():
    assert hasVowel("borg") == True

def test_hasVowel_5():
    assert hasVowel("frEE") == True



from lab03 import isNumber

# Tests for isNumber
def test_isNumber_1():
    assert isNumber("1") == False

def test_isNumber_2():
    assert isNumber(-1) == True

def test_isNumber_3():
    assert isNumber(True) == False

def test_isNumber_4():
    assert isNumber(3.14) == True

def test_isNumber_5():
    assert isNumber([0]) == False


from lab03 import onlyContainsStrings

# Tests for onlyContainsStrings
def test_onlyContainsStrings_1():
    assert onlyContainsStrings([]) == False

def test_onlyContainsStrings_2():
    assert onlyContainsStrings(["a", "c", ""]) == True

def test_onlyContainsStrings_3():
    assert onlyContainsStrings(["18", 18, "eighteen"]) == False
    
def test_onlyContainsStrings_4():
    assert onlyContainsStrings([-1, "-1"]) == False

def test_onlyContainsStrings_5():
    assert onlyContainsStrings("python") == False


