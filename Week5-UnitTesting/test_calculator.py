# Importing square funciton form calculator.py
from calculator import square
from hello import hello

# This integrates the library named pytest
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_hello_argument():
    assert hello("Delstun") == "Hello! Delstun"

def test_hello_default():
    assert hello() == "Hello! world"

#def main():
#    test_square()

# There are a few ways you could write this, you could use an if statement however it could make codebase larger. You could also use an assertion however it is not very user-friendly, however you can use a `try` and `except`
# But you might run into the same issue as before by making the codebase larger.
#def test_square():
#    try:
#        assert square(2) == 4
#    except AssertionError:
#        print("2 squared was not 4")
#    
#    try:
#        assert square(3) == 9
#    except AssertionError:
#        print("3 sqaured was not 9")

# if __name__ == "__main__":
#     main()