def rank_recommendations(recommendations):
    return sorted(recommendations, key=lambda item: item["score"], reverse=True)

def display_recommendations(recommendations):
    print("\n===== PERSONALIZED RECOMMENDATIONS =====")
    if not recommendations:
        print("No recommendations available.")
        return
    for rank, item in enumerate(recommendations, start=1):
        print(f"\n{rank}. {item['title']}")
        print(f"   Score: {item['score']}%")
        print(f"   Reason: {item['reason']}")
        print(f"   Explanation: {item['explanation']}")

    print("\n===== RECOMMENDATION RANKING =====")
    print(f"{'Rank':<8}{'Recommendation':<38}{'Score'}")
    print("-" * 58)
    for rank, item in enumerate(recommendations, start=1):
        print(f"{rank:<8}{item['title'][:36]:<38}{item['score']}%")
