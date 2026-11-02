from input_module import collect_profile
from profile_module import analyze_profile
from prompt_module import build_prompt
from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations, display_recommendations
from feedback_module import collect_feedback
from explanation_module import explain_recommendation
from intent_module import detect_intent
from save_module import save_recommendations

MENU_INTENTS = {
    "1": "GENERATE_RECOMMENDATION",
    "2": "REFINE_RECOMMENDATION",
    "3": "SHOW_PROFILE",
    "4": "EXPLAIN_RECOMMENDATION",
    "5": "SAVE_RECOMMENDATION",
    "6": "EXIT",
}

def make_recommendations(profile, analysis, feedback=""):
    prompt = build_prompt(profile, analysis, feedback)
    results = generate_recommendations(prompt)
    results = rank_recommendations(results)
    display_recommendations(results)
    return results

def main():
    print("=" * 55)
    print(" PERSONALIZED RECOMMENDATION SYSTEM - OLLAMA")
    print("=" * 55)
    print("Make sure Ollama is running and llama3.2 is installed.")

    profile = collect_profile()
    analysis = analyze_profile(profile)
    feedback = ""
    try:
        recommendations = make_recommendations(profile, analysis)
    except Exception as error:
        print("\nCould not generate recommendations:", error)
        print("Check Ollama is running and run: ollama pull llama3.2")
        return

    while True:
        print("\n===== MENU =====")
        print("1. Generate recommendations")
        print("2. Refine recommendations using feedback")
        print("3. Show profile")
        print("4. Explain a recommendation")
        print("5. Save recommendations")
        print("6. Exit")
        user_input = input("\nChoose 1-6 or type a request: ").strip()

        try:
            intent = MENU_INTENTS.get(user_input) or detect_intent(user_input)
            print("Detected Intent:", intent)

            if intent == "GENERATE_RECOMMENDATION":
                recommendations = make_recommendations(profile, analysis, feedback)

            elif intent == "REFINE_RECOMMENDATION":
                feedback = collect_feedback()
                recommendations = make_recommendations(profile, analysis, feedback)

            elif intent == "SHOW_PROFILE":
                print("\n===== USER PROFILE =====")
                for key, value in profile.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
                print("\n===== PREFERENCE ANALYSIS =====")
                for key, value in analysis.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")

            elif intent == "EXPLAIN_RECOMMENDATION":
                explain_recommendation(recommendations)

            elif intent == "SAVE_RECOMMENDATION":
                save_recommendations(profile, recommendations)

            elif intent == "EXIT":
                print("Thank you for using the Personalized Recommendation System!")
                break

            else:
                print("Intent not recognized. Please try again.")

        except Exception as error:
            print("This operation failed:", error)
            print("Check that Ollama is running and the llama3.2 model is installed.")

if __name__ == "__main__":
    main()
