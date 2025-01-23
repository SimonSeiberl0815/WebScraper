import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)


def get_course_summary(description : str, type : str):
    if description == None or description == '' or description == 'keine':
        return 'keine'

    prompt = f"Given the following {type} of a course, summerize and list the {type} of the course in a few words seperated by a newline with no bullet points in german :\n{description}"
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    goals_text = response.text
    return goals_text
