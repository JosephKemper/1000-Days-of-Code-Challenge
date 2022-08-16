# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    user_gender = input ("Please enter your gender (M or F): ")
    user_birth_date = input ("Enter your birthdate (YYYY-MM-DD): ")
    user_weight = float(input ("Enter your weight in U.S. pounds: "))
    user_height = float(input ("Enter your height in U.S. inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age_user = compute_age(user_birth_date)
    weight_in_kilos = kg_from_lb(user_weight)
    height_in_cm = cm_from_in(user_height)
    bmi_user = body_mass_index(height=height_in_cm,weight=weight_in_kilos)
    bmr_user = basal_metabolic_rate (gender=user_gender,weight=weight_in_kilos,height=height_in_cm,age=age_user)

    # Print the results for the user to see.
    print(f"Age (years): {age_user}")
    print(f"Weight (kg): {weight_in_kilos:.2f}")
    print(f"Height (cm): {height_in_cm:.1f}")
    print(f"Body mass index: {bmi_user:.2f}")
    print(f"Basal metabolic rate (kcal/day): {bmr_user:.0f}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight_in_kilos = pounds*0.45359237
    return weight_in_kilos


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height_in_cm = inches * 2.54
    return height_in_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000*weight)/(height*height)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    bmr = 0
    if gender.lower() == "m":
        bmr = 88.362 + 13.39 * weight + 4.799 * height - 5.677 * age
    elif gender.lower() == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()