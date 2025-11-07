"""
File: class_reviews.py
Name: Zoe
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

def main():
    """
    Calculates the min, max, avg of sc001 and sc101. Program exits when -1 is inserted
    """
    # initial variables
    counter_001 = 0
    counter_101 = 0
    score_total_001 = 0
    score_total_101 = 0
    max_001 = 0
    min_001 = 0
    max_101 = 0
    min_101 = 0

    while True:
        class_name = input('Which Class? ')
        if class_name == '-1':
            break
        else:
            # sc001 calculations
            if class_name.lower() == 'sc001':
                counter_001 += 1
                score = int(input('Score:'))
                if counter_001 == 1:
                    max_001 = score
                    min_001 = score
                else:
                    if score > max_001:
                        max_001 = score
                    if score < min_001:
                        min_001 = score
                score_total_001 += int(score)
            # sc002 calculations
            if class_name.lower() == 'sc101':
                counter_101 += 1
                score = int(input('Score:'))
                if counter_101 == 1:
                    max_001 = score
                    min_001 = score
                else:
                    if score > max_101:
                        max_101 = score
                    if score < min_101:
                        min_101 = score
                score_total_101 += int(score)
    # print outputs
    print('=======SC001=========')
    if counter_001 != 0:
        print('Max(001):', max_001)
        print('Min(001):', min_001)
        print('Avg(001):', score_total_001 / counter_001)
    else:
        print('No score for 001')
    print('=======SC101=========')
    if counter_101 != 0:
        print('Max(101):', max_001)
        print('Min(101):', min_001)
        print('Avg(101):', score_total_001 / counter_001)
    else:
        print('No Score for 101')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__ == '__main__':
    main()
