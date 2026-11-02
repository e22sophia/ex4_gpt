def explain_recommendation(recommendations):
    if not recommendations:
        print("No recommendations available. Generate some first.")
        return
    print("\nAvailable recommendations:")
    for i, item in enumerate(recommendations, start=1):
        print(f"{i}. {item['title']}")
    try:
        choice = int(input("Select a recommendation number: "))
        if not 1 <= choice <= len(recommendations):
            print("Invalid recommendation number.")
            return
        item = recommendations[choice - 1]
        print("\n===== RECOMMENDATION EXPLANATION =====")
        print("Name:", item["title"])
        print("Suitability score:", f"{item['score']}%")
        print("Reason:", item["reason"])
        print("Explanation:", item["explanation"])
    except ValueError:
        print("Please enter a valid number.")
