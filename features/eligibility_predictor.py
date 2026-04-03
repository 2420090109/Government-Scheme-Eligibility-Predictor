def check_eligibility(age, income, category):

    schemes = []

    if age >= 18 and income < 200000:
        schemes.append("PM Awas Yojana")

    if category == "student":
        schemes.append("National Scholarship")

    if category == "farmer":
        schemes.append("PM Kisan")

    return schemes