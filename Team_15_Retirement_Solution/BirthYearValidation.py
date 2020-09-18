def birth_year_validation(year):
    try:
        year = int(year)
        if year < 1900:
            print("Please try again. Year should be 1900 or more recent")
            return False
        else:
            return True
    except ValueError:
        print("Value should be a number, Please try again")
        return False
