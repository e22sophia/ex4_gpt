import json
import ollama

MODEL = "llama3.2"

def generate_recommendations(prompt):
    print("\nGenerating recommendations using Ollama...")
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You generate personalized recommendations. "
                    "Follow the requested JSON structure exactly."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        format="json",
    )
    content = response["message"]["content"]
    data = json.loads(content)
    recommendations = data.get("recommendations", [])
    if not isinstance(recommendations, list) or not recommendations:
        raise ValueError("The model did not return a valid recommendations list.")

    cleaned = []
    for item in recommendations:
        try:
            score = int(item.get("score", 0))
        except (TypeError, ValueError):
            score = 0
        cleaned.append({
            "title": str(item.get("title", "Untitled recommendation")),
            "score": max(0, min(100, score)),
            "reason": str(item.get("reason", "No reason provided.")),
            "explanation": str(item.get("explanation", "No explanation provided.")),
        })
    return cleaned
