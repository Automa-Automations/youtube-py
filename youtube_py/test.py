from tests import TestCreateChannel
import unittest

tests = {
    "test_create_channel": TestCreateChannel
}

def main():
    for index, test in enumerate(tests):
        print(f"{index+1}. {test}")
    choice = int(input("Enter the number of the test you want to run: "))
    test = list(tests.values())[choice-1]
    test = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner().run(test)

main()
