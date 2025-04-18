import google.generativeai as genai

API_KEY = "enter-gemini-api-key"
genai.configure(api_key=API_KEY)

def generate_script(title, description):
    prompt = f"""
    You're a news anchor. Write a short 30–60 second news segment script based on the following:

    Title: {title}
    Description: {description}

    The script should sound informative, engaging, and natural for voiceover. Keep it concise.
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return response.text

# Example usage
if __name__ == "__main__":
    # Example from newsapi
    title = "New Solar Tech Promises Cheaper Renewable Energy"
    description = "Scientists have unveiled a breakthrough in solar cell materials that could significantly cut costs and boost efficiency for mass adoption."
    
    script = generate_script(title, description)
    print("\n Generated Script:\n")
    print(script)
