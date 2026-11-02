# Personalized Recommendation System using Ollama

A modular Python console application for Experiment 4. It collects a user profile,
analyzes preferences, generates and ranks recommendations, explains results,
accepts feedback, detects intent, and saves recommendations to a text file.

## Requirements
- Windows, Python 3.10 or newer
- Ollama installed: https://ollama.com/download/windows
- The `llama3.2` model

## Setup (Windows PowerShell)
```powershell
cd RecommendationSystem
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
ollama pull llama3.2
```

Ensure Ollama is running (open the Ollama desktop app; or run `ollama serve` in a
separate terminal), then run:
```powershell
python main.py
```

## Features
- User profile collection and preference analysis
- Prompt construction and Ollama recommendation generation
- Suitability scoring and ranking
- Per-item explanations
- Feedback-based refinement
- LLM intent detection for six intents
- Saving recommendations to `outputs/recommendations.txt`

## Notes
- Model-generated scores are estimates, not validated probabilities.
- Recommendations are generated locally by Ollama. Output quality depends on the model.
- If intent detection misclassifies a message, use the numbered menu.
