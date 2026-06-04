from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os
from datetime import datetime

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]
)


def generate_study_plan(
    exam,
    exam_date,
    exam_format,
    subject_data,
    hours,
    burnout,
    consistency,
    extra_context
):

    # ========================
    # CALCULATE KEY METRICS
    # ========================

    days_remaining = (exam_date - datetime.now().date()).days
    days_remaining = max(days_remaining, 1)

    total_chapters = sum(
        s["chapters_remaining"]
        for s in subject_data.values()
    )

    avg_confidence = (
        sum(
            s["confidence"]
            for s in subject_data.values()
        ) / len(subject_data)
    ) if len(subject_data) > 0 else 0

    total_study_hours = days_remaining * hours

    chapters_per_day = (
        total_chapters / days_remaining
        if days_remaining > 0
        else 0
    )

    # ========================
    # SYSTEM PROMPT
    # ========================

    system_prompt = """
You are DAY-1NE, an honest strategist built for overwhelmed students and learners.

Your core values:
- NEVER use motivational platitudes
- ALWAYS be brutally honest
- PRIORITIZE realism over optimism
- REJECT generic productivity advice
- FOCUS on execution
- ACKNOWLEDGE burnout and consistency issues

Before answering:
1. Understand what the user is actually trying to achieve.
2. Decide whether this is:
   - Exam Preparation
   - Skill Learning
   - Career Development
   - General Productivity
3. Adapt accordingly.

Your tone:
calm, mature, direct, practical.
"""

    # ========================
    # BUILD SUBJECT BREAKDOWN
    # ========================

    subject_breakdown = ""

    for subject, data in subject_data.items():

        topics_str = data.get("topics", "").strip()

        if topics_str:
            subject_breakdown += (
                f"- {subject}: "
                f"{data['chapters_remaining']} topics/chapters | "
                f"Confidence: {data['confidence']}/10 | "
                f"Remaining Topics: {topics_str}\n"
            )
        else:
            subject_breakdown += (
                f"- {subject}: "
                f"{data['chapters_remaining']} topics/chapters | "
                f"Confidence: {data['confidence']}/10\n"
            )

    # ========================
    # DETECT SKILL LEARNING
    # ========================

    combined_text = (
        exam.lower()
        + " "
        + (extra_context.lower() if extra_context else "")
        + " "
        + " ".join(subject.lower() for subject in subject_data.keys())
    )

    skill_keywords = [
        "dsa",
        "leetcode",
        "coding",
        "programming",
        "web development",
        "webdev",
        "frontend",
        "backend",
        "python",
        "java",
        "c++",
        "javascript",
        "machine learning",
        "ml",
        "ai",
        "artificial intelligence",
        "data science",
        "skill",
        "learn"
    ]

    is_skill_learning = any(
        keyword in combined_text
        for keyword in skill_keywords
    )

    # ========================
    # SKILL LEARNING MODE
    # ========================

    if is_skill_learning:

        prompt = f"""
USER PROFILE
================

Learning Goal:
{exam}

Topics / Skills:
{subject_breakdown}

Available Hours Per Day:
{hours}

Burnout:
{burnout}

Consistency:
{consistency}

Additional Context:
{extra_context if extra_context else "None provided"}

================
YOUR TASK
================

The user is trying to learn a skill.

Do NOT treat this as an exam.

Think like an experienced mentor.

Understand:
- current level
- learning goal
- available time
- realistic progress expectations

Where specific topics are listed for a skill area, use them directly
to sequence the roadmap. Do NOT invent generic topic lists if the
user has already provided their own.

OUTPUT FORMAT:

## 🎯 LEARNING ASSESSMENT
Assess their current situation.

## 🗺️ RECOMMENDED ROADMAP
Suggest the ideal topic order. If the user listed specific topics,
sequence THOSE topics. Do not substitute with generic ones.

## 📅 30-DAY PLAN
Give a week-by-week roadmap referencing the user's actual topics.

## 💡 DAILY LEARNING SYSTEM
Show how to use {hours} hours/day.

## ⚠️ COMMON MISTAKES TO AVOID
Specific mistakes beginners make with these exact topics.

## 🚀 NEXT MILESTONE
What success should look like after 30 days.

CRITICAL RULES:

- Do NOT discuss exam pressure.
- Do NOT discuss syllabus completion.
- Do NOT invent academic risks.
- Focus on skill acquisition.
- Be practical and specific.
- Reference the user's actual topic names wherever possible.
"""

    # ========================
    # EXAM MODE
    # ========================

    else:

        prompt = f"""
STUDENT PROFILE
================

Exam:
{exam}

Exam Date:
{exam_date}

Days Remaining:
{days_remaining}

Exam Format:
{exam_format}

ACADEMICS:

- Total Topics Remaining: {total_chapters}
- Topics Per Day Needed: {chapters_per_day:.2f}
- Average Confidence: {avg_confidence:.1f}/10
- Total Available Study Hours: {total_study_hours}

SUBJECT BREAKDOWN:

{subject_breakdown}

EXECUTION CAPACITY:

- Hours Per Day: {hours}
- Burnout: {burnout}
- Consistency: {consistency}

ADDITIONAL CONTEXT:

{extra_context if extra_context else "None provided"}

================
YOUR TASK
================

Analyze this student's situation.

Where specific topic names are listed under a subject, use them
directly in your recommendations. Prioritize, sequence, and
reference those exact topics. Do NOT replace them with generic ones.

OUTPUT FORMAT:

## 📊 SITUATION ANALYSIS

## ⚠️ CRITICAL WEAK AREAS
Call out specific topics by name where confidence is low.

## 🎯 PRIORITY STRATEGY
Which topics to hit first and why, referencing actual topic names.

## 📋 REALISTIC ALLOCATION PLAN
Day-by-day or week-by-week plan using the listed topics.

## 💡 DAILY EXECUTION BLUEPRINT

## 🚨 BURNOUT + CONSISTENCY REALITY CHECK

## 🎓 HONEST FINAL ADVICE

CRITICAL RULES:

- Be brutally realistic.
- Mention feasibility clearly.
- Account for confidence levels.
- Account for burnout.
- Avoid generic advice.
- Focus on practical execution.
- Reference the user's actual topic names wherever possible.
"""

    # ========================
    # CALL GROQ
    # ========================

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=2000
    )

    return response.choices[0].message.content