import os
from get_trending_news import get_top_headlines
from generate_script import generate_script

OUTPUT_FOLDER = r"C:\vscode\Synergylabs Technology\video_inputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def create_inputs():
    headlines = get_top_headlines(limit=3)

    for idx, article in enumerate(headlines, start=1):
        title = article['title']
        description = article['description'] or ""
        script = generate_script(title, description)

        # Save script
        script_file = os.path.join(OUTPUT_FOLDER, f"{idx}_script.txt")
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(script.strip())

        # Suggest 3 keyword-based image prompts
        keywords = [title] + description.split()[:10]
        prompts = [f"Image suggestion: {kw}" for kw in keywords[:3]]

        image_file = os.path.join(OUTPUT_FOLDER, f"{idx}_images.txt")
        with open(image_file, "w", encoding="utf-8") as f:
            f.write("\n".join(prompts))

        print(f"[{idx}] Script & image prompts saved.")

if __name__ == "__main__":
    create_inputs()
