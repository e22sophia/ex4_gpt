import json
import ollama

MODEL = "llama3.2"
VALID_INTENTS = {
    "GENERATE_RECOMMENDATION",
    "REFINE_RECOMMENDATION",
    "SHOW_PROFILE",
    "EXPLAIN_RECOMMENDATION",
    "SAVE_RECOMMENDATION",
    "EXIT",
}

def detect_intent(user_input):
    prompt = f"""
Classify the user message into exactly one of these intents:
GENERATE_RECOMMENDATION, REFINE_RECOMMENDATION, SHOW_PROFILE,
EXPLAIN_RECOMMENDATION, SAVE_RECOMMENDATION, EXIT.

Examples:
"Recommend AI courses" -> GENERATE_RECOMMENDATION
"Give me beginner-friendly options" -> REFINE_RECOMMENDATION
"Show my details" -> SHOW_PROFILE
"Why did you recommend this?" -> EXPLAIN_RECOMMENDATION
"Save my recommendations" -> SAVE_RECOMMENDATION
"Exit" -> EXIT

Return JSON only: {{"intent": "ONE_VALID_INTENT"}}
User message: {json.dumps(user_input)}
"""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        format="json",
    )
    try:
        intent = json.loads(response["message"]["content"]).get("intent", "").upper()
    except (json.JSONDecodeError, KeyError, TypeError):
        intent = ""
    if intent not in VALID_INTENTS:
        # Safe fallback: treat unclear requests as a refinement request.
        return "REFINE_RECOMMENDATION"
    return intent
