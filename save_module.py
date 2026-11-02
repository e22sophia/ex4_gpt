from pathlib import Path
from datetime import datetime

def save_recommendations(profile, recommendations):
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "recommendations.txt"
    with file_path.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write("Saved on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(f"User: {profile.get('name', '')}\n")
        file.write(f"Goal: {profile.get('goal', '')}\n\n")
        for rank, item in enumerate(recommendations, start=1):
            file.write(f"{rank}. {item['title']}\n")
            file.write(f"Score: {item['score']}%\n")
            file.write(f"Reason: {item['reason']}\n")
            file.write(f"Explanation: {item['explanation']}\n\n")
    print(f"Recommendations saved to: {file_path.resolve()}")
