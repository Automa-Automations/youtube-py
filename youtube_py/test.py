import tests 
import unittest

tests = {
    "test_create_channel": tests.TestCreateChannel,
    "test_create_video": tests.TestCreateVideo,
    "test_create_community_post": tests.TestCreateCommunityPost,
    "test_delete_channel": tests.TestDeleteChannel,
}

def main():
    # Option 0: Run all tests
    print("0. Run all tests")
    for index, test in enumerate(tests):
        print(f"{index+1}. {test}")
    choice = int(input("Enter the number of the test you want to run: "))
    if choice == "0":
        # run all tests
        suite = unittest.TestSuite()
        # continue
        suite.addTests([unittest.TestLoader().loadTestsFromTestCase(test) for test in tests.values()])
        unittest.TextTestRunner().run(suite)
    test = list(tests.values())[choice-1]
    test = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner().run(test)

main()
