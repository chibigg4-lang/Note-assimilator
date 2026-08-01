import os
import time
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = api_key)
PROMPT = """
Transcribe this note image exactly into Markdown.

Rules:
- Do not summarize.
- Do not translate Vietnamese.
- Preserve mathematical notation using LaTeX.
- Wrap display formulas in $$ ... $$.
- Wrap code in Markdown code fences.
- Keep headings, bullet points, and numbering if visible.
- If something is unreadable, write [unreadable].
- Return only the extracted Markdown.
"""

def extract_markdown_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    model = genai.GenerativeModel("gemini-3.1-flash-lite")
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # 1. Try to send the image to Gemini
            response = model.generate_content([PROMPT, image])
            return response.text
            
        except Exception as e:
            # 2. If it fails, check if it's a Rate Limit/Quota error
            error_message = str(e)
            if "429" in error_message or "Quota" in error_message:
                print(f"⚠️ API Speed Limit hit! Waiting 35 seconds... (Retry {attempt + 1}/{max_retries})")
                time.sleep(35) # Sleep for 35 seconds to let the Google quota reset
            else:
                # If it's a completely different error, crash normally
                raise e
                
    # If it fails 5 times in a row, give up cleanly
    raise Exception(f"Failed to process {image_path} after 5 retries due to strict API limits.")
