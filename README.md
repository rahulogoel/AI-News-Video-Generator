# AI Video Generation Tool
This project automatically generates short videos based on trending news articles using AI for scriptwriting and video generation tools like Lumen5.

## Demo
https://github.com/user-attachments/assets/52f87e5f-ac93-48f6-8e77-1bb7dc985f0f

Also checkout *9:15 format size* video and more at `generated_video` folder.

## Features
- Scrapes top headlines from [NewsAPI](https://newsapi.org/)
- Uses Gemini 2.0 Flash AI to write a 30–60 second news script
- Prepares scripts and image prompts for video creation
- Final video is generated using Lumen5 GenAI video tool

## Project Structure
```
AI_Video_Generation_Tool/
├── README.md
├── Report.pdf
├── get_trending_news.py
├── create_video_inputs.py
├── generate_script.py
├── video_inputs/
│   ├── 1_script.txt
│   ├── 1_images.txt
│   └── ...
├── generated_video/
│   └── Bond_Market_Update_Tonight.mp4
│   └── Nvidia_RTX_5060_Ti_Launch_Update.mp4
└── requirements.txt
```

## Setup Instructions

### 1. Install requirements
```bash
pip install requests google-generativeai
```

### 2. Set API Keys
- [NewsAPI Key](https://newsapi.org)
- [Gemini API Key](https://aistudio.google.com/app/apikey)

### 3. Run the Pipeline
```bash
python create_video_inputs.py
```

## Report
Detailed pipeline explanation, tools used, and future improvements:
[Download Report (PDF)](./Report.pdf)

## Future Work
- Deploy as a Streamlit app
- Add text-to-speech for narration
- Increase video engagement features and accuracy/quality of news
- Fully automate video rendering (using MoviePy or GenAI APIs like RunwayML).

