def collect_profile():
    print("\n===== USER PROFILE COLLECTION =====")
    profile = {
        "name": input("Enter name: ").strip(),
        "age": input("Enter age: ").strip(),
        "background": input("Educational/Professional background: ").strip(),
        "interests": input("Enter interests (comma-separated): ").strip(),
        "skill_level": input("Skill level (Beginner/Intermediate/Advanced): ").strip(),
        "preference": input("Preferred category or learning style: ").strip(),
        "goal": input("Enter your goal: ").strip(),
        "number": input("Number of recommendations: ").strip(),
    }
    try:
        count = int(profile["number"])
        if count < 1:
            raise ValueError
        profile["number"] = min(count, 20)
    except ValueError:
        print("Invalid number. Using 5 recommendations.")
        profile["number"] = 5

    print("\n===== COLLECTED PROFILE =====")
    for key, value in profile.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    return profile
