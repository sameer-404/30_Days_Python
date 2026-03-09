#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month.lower() in ["december", "january", "february"]:
        return "Winter"
    elif month.lower() in ["march", "april", "may"]:
        return "Spring"
    elif month.lower() in ["june", "july", "august"]:
        return "Summer"
    elif month.lower() in ["september", "october", "november"]:
        return "Autumn"
    else:
        return "Invalid month!"


print(check_season("June"))   # Summer
print(check_season("JANUARY")) # Winter
print(check_season("hello"))  # Invalid month!