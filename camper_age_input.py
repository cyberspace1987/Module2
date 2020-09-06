"""
Program: camper_age_input.py
Author: Cara Krug
Last date modified: 09/06/2020

Program specifications: The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp
and convert the age in months to years via a function call then print the result.
"""
def main():
    print('Enter age in years: ')
    age_in_years = float(input())
    age_in_months = convert_to_months(age_in_years)
    print(age_in_months)


def convert_to_months(age_in_years):
    return age_in_years * 12


if __name__ == '__main__':
    main()
