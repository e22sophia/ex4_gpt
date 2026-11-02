def analyze_profile(profile):
    interests = [x.strip() for x in profile["interests"].split(",") if x.strip()]
    analysis = {
        "primary_interest": interests[0] if interests else "General",
        "secondary_interest": interests[1] if len(interests) > 1 else "None",
        "skill_level": profile["skill_level"],
        "goal": profile["goal"],
        "preference": profile["preference"],
        "important_constraints": (
            f"Skill level: {profile['skill_level']}; "
            f"preferred category/learning style: {profile['preference']}"
        ),
    }
    print("\n===== PREFERENCE ANALYSIS =====")
    for key, value in analysis.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    return analysis
