def score_input()
    test_name = input('What is the test name? ')
    test_score = int(input('What is the test score? '))
        if test_score in (0-100):
            return 'Invalid test score, try again!'