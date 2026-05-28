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
    total_chapters = sum(s["chapters_remaining"] for s in subject_data.values())
    avg_confidence = (sum(s["confidence"] for s in subject_data.values()) / len(subject_data)) if len(subject_data) > 0 else 0
    total_study_hours = days_remaining * hours
    chapters_per_day = total_chapters / days_remaining if days_remaining > 0 else 0
    
    # ========================
    # SYSTEM PROMPT
    # ========================
    
    system_prompt = """You are DAY-1NE, an honest academic strategist built for overwhelmed students.

Your core values:
- NEVER use motivational platitudes or fake hype
- ALWAYS be brutally honest about feasibility
- PRIORITIZE clarity and realism over optimism
- REJECT generic productivity advice
- FOCUS on execution over fantasy planning
- ACKNOWLEDGE burnout and consistency challenges

You analyze academic situations with surgical precision and deliver actionable, realistic roadmaps.
Your tone: calm, mature, direct, compassionate but honest."""

    # ========================
    # BUILD SUBJECT BREAKDOWN
    # ========================
    
    subject_breakdown = ""
    for subject, data in subject_data.items():
        subject_breakdown += f"- {subject}: {data['chapters_remaining']} topics/chapters | Confidence: {data['confidence']}/10\n"
    
    # ========================
    # MAIN PROMPT
    # ========================
    
    prompt = f"""
STUDENT PROFILE:
================

Exam: {exam}
Exam Date: {exam_date} ({days_remaining} days away)
Exam Format: {exam_format}

ACADEMICS:
- Total Topics/Chapters Remaining: {total_chapters}
- Topics Per Day Needed (if uniform): {chapters_per_day:.2f}
- Average Confidence Across Subjects: {avg_confidence:.1f}/10
- Total Available Study Hours: {total_study_hours} hours

SUBJECT BREAKDOWN:
{subject_breakdown}

EXECUTION CAPACITY:
- Study Hours/Day: {hours}
- Burnout Level: {burnout}
- Consistency: {consistency}

ADDITIONAL CONTEXT:
{extra_context if extra_context else "None provided"}

================
YOUR TASK:
================

Analyze this student's situation and provide a REALISTIC, STRUCTURED strategy.

OUTPUT FORMAT (Follow exactly):

## 📊 SITUATION ANALYSIS
[Honest assessment of feasibility. Include: time pressure, workload realism, confidence gaps, risk factors]

## ⚠️ CRITICAL WEAK AREAS
[Rank subjects/areas by risk (1=highest risk). Which subjects have lowest confidence + highest workload?]

## 🎯 PRIORITY STRATEGY
[For {exam}, what's the smart prioritization? Which subjects matter most? Which can be optimized?]

## 📋 REALISTIC ALLOCATION PLAN
[Show how to distribute {hours} hours/day across {len(subject_data)} subject(s) over {days_remaining} days]

## 💡 DAILY EXECUTION BLUEPRINT
[Give a sample daily routine with specific subjects/topics. Be concrete.]

## 🚨 BURNOUT + CONSISTENCY REALITY CHECK
[Their burnout is {burnout} and consistency is {consistency}. Is this sustainable? What needs adjustment?]

## 🎓 HONEST FINAL ADVICE
[End with 2-3 sentences of real, grounded guidance. No BS - just truth.]

================
CRITICAL RULES:
================
- If completing all chapters is unrealistic, say it. Suggest damage-control prioritization.
- Account for their confidence levels - weaker subjects need more time
- Their consistency level ({consistency}) matters: if "Very Poor", suggest smaller daily commitments
- With {burnout} burnout level, don't suggest unsustainable schedules
- Be specific about which topics/chapters to focus on vs. which to optimize/skip
- Don't use generic productivity tips - focus on their specific subjects and timeline
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