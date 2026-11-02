import json

def build_prompt(profile, analysis, feedback=""):
    return f"""
You are a personalized recommendation assistant.

USER PROFILE:
{json.dumps(profile, ensure_ascii=False, indent=2)}

PREFERENCE ANALYSIS:
{json.dumps(analysis, ensure_ascii=False, indent=2)}

USER FEEDBACK:
{feedback or "No feedback provided."}

Generate exactly {profile['number']} recommendations. Respect all user constraints
and explicitly exclude topics the user rejects. Match the user's interests,
goal, background, preferences, and skill level. Rank recommendations from
most suitable to least suitable.

Return JSON only in this structure:
{{
  "recommendations": [
    {{
      "title": "Recommendation name",
      "score": 95,
      "reason": "Short reason for recommending it",
      "explanation": "Detailed explanation of suitability"
    }}
  ]
}}

Scores must be integers from 0 to 100 and are estimates, not probabilities.
Do not include markdown fences or any text outside the JSON.
"""
