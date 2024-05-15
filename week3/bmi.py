# team activty 1/16/34

from datetime import datetime

def get_gender():
    return input("Please enter your gender (M or F): ").lower()

def get_birthday():
    return input("Enter your birthdate (YYYY-MM-DD): ")

def get_weight():
    return int(input("Enter your weight in U.S. pounds: "))

def get_height():
    return int(input("Enter your height in U.S. inches: "))

def convert_lbs_kg(lbs):
    return lbs * 0.45359237

def convert_in_cm(inches):
    return inches * 2.54



def calculate_bmi(weight, height):
    return 10000 * weight / height / height

def calculate_bmr(gender, age, weight, height):
    if gender == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age          
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

def dispay(age, weight, height, bmi, bmr):
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight}")
    print(f"Height (m): {height / 100}")
    print(f"Body mass index: {bmi}")
    print(f"Basal metabolic rate (kcal/day): {bmr}")

def calculate_age(birth_str):
    today = datetime.now()
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")

    print(birthdate)
    print(birthdate.year)

    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years - 3


def main():
    gender = get_gender()
    weight_lbs = get_weight()
    height_in = get_height()
    birthday = get_birthday()

    weight_kg = convert_lbs_kg(weight_lbs)
    height_m = convert_in_cm(height_in)

    age = calculate_age(birthday)

    dispay(age, weight_kg, height_m, calculate_bmi(weight_kg, height_m), calculate_bmr(gender, age, weight_kg, height_m))
    


main()