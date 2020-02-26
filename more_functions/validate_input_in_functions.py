def score_input():
    test_name = input('What is the test name? ')
    test_score = int(input('What is the test score? '))
    if test_score > 100:
        print('Invalid test score, try again!')
    elif 0 < test_score < 100:
        print(test_name, test_score)

if __name__ == '__main__':
    score_input()
