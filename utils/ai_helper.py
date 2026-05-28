from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Function to generate AI study plan
def generate_study_plan(exam, subjects, hours, confidence):

    prompt = f"""
    A student is preparing for {exam}.

    Subjects: {subjects}

    Study hours available daily: {hours}

    Confidence level: {confidence}

    Generate a realistic and practical study strategy.

    Keep it concise, structured, and motivating without being unrealistic.
    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content