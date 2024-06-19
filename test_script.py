import student_code
import sys


def grade_assignment():
    score = 0
    total_questions = 4

    # Question 1: Check if "Conveyor Belt" is added.
    if "Conveyor Belt" in student_code.equipment:
        score += 1
    else:
        print("Question 1 failed: 'Conveyor Belt' not added to equipment list.")

    # Question 2: Check if "Scratch" is removed.
    if "Scratch" not in student_code.defects:
        score += 1
    else:
        print("Question 2 failed: 'Scratch' not properly removed from defects list.")

    # Question 3: Check if the total stock in warehouse 2 is correct.
    expected_total_stock_warehouse_2 = sum([320, 210, 150])
    if student_code.total_stock_warehouse_2 == expected_total_stock_warehouse_2:
        score += 1
    else:
        print("Question 3 failed: Incorrect total stock for warehouse 2.")

    # Question 4: Check if boolean list for even numbers is correct.
    expected_is_even = [False, True, False, True, False, True]
    if student_code.is_even == expected_is_even:
        score += 1
    else:
        print("Question 4 failed: Incorrect list comprehension for even numbers.")

    # Final grading
    if score == total_questions:
        sys.exit(0)  # Pass
    else:
        sys.exit(1)  # Fail


grade_assignment()
