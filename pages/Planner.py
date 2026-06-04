import streamlit as st

from utils.ai_helper import generate_study_plan

st.set_page_config(
    page_title="Planner",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Study Planner")

st.markdown("""
Create a realistic and personalized study strategy
based on your actual academic situation.
""")

st.divider()

# =========================
# INITIALIZE SESSION STATE
# =========================

if "subjects_list" not in st.session_state:
    st.session_state.subjects_list = []

if "clear_input" not in st.session_state:
    st.session_state.clear_input = False

# =========================
# MAIN FORM (STARTS HERE)
# =========================

with st.form("planner_form"):

    # =========================
    # EXAM CONTEXT (FIRST)
    # =========================

    st.subheader("🎯 Exam Context")

    exam = st.selectbox(
        "Exam Name",
        ["JEE", "NEET", "Boards", "Semester", "Other"]
    )

    custom_exam = ""

    if exam == "Other":
        custom_exam = st.text_input(
            "Enter Exam Name"
        )

    exam_date = st.date_input(
        "Exam Date"
    )

    exam_format = st.radio(
        "Exam Format",
        ["MCQ", "Subjective", "Mixed"],
        horizontal=True
    )

    st.divider()

    # =========================
    # SUBJECT ANALYSIS (SECOND)
    # =========================

    st.subheader("📚 Subject Analysis")

    st.markdown("**Add subjects dynamically** (e.g., DS, Algo, CPC, MATLAB, Graphics, Mechanics)")

    # Clear input if flag is set
    input_value = "" if st.session_state.clear_input else st.session_state.get("new_subject_input", "")
    if st.session_state.clear_input:
        st.session_state.clear_input = False

    # Input area for new subject
    col1, col2 = st.columns([3, 1])

    with col1:
        new_subject = st.text_input(
            "Subject Name",
            value=input_value,
            placeholder="e.g., Data Structures, Algorithms, MATLAB...",
            key="new_subject_input"
        )

    with col2:
        add_subject_btn = st.form_submit_button(
            "➕ Add Subject",
            use_container_width=True
        )

    # Handle adding subject (within form logic)
    if add_subject_btn and new_subject:
        if new_subject.strip() not in st.session_state.subjects_list:
            st.session_state.subjects_list.append(new_subject.strip())
            st.session_state.clear_input = True
            st.rerun()
        else:
            st.warning(f"'{new_subject}' already added!")

    # Display added subjects
    if st.session_state.subjects_list:
        st.markdown("**Selected Subjects:**")
        
        cols = st.columns(3)
        for idx, subject in enumerate(st.session_state.subjects_list):
            with cols[idx % 3]:
                st.info(subject)

    st.divider()

    # ========================
    # SUBJECT DETAILS (THIRD)
    # ========================

    if st.session_state.subjects_list:
        st.markdown("**Enter details for each subject:**")
        
        subject_data = {}

        for subject in st.session_state.subjects_list:

            st.markdown(f"### {subject}")

            col1, col2 = st.columns(2)

            with col1:

                chapters_remaining = st.number_input(
                    f"Chapters/Topics Remaining",
                    min_value=0,
                    max_value=100,
                    value=10,
                    step=1,
                    key=f"chapters_{subject}"
                )

            with col2:

                confidence = st.slider(
                    f"Confidence Level",
                    1,
                    10,
                    5,
                    key=f"confidence_{subject}"
                )

            topics_remaining = st.text_area(
                f"Topics Remaining",
                placeholder="e.g., SHM, Rotation, Electrostatics, Modern Physics",
                key=f"topics_{subject}",
                help="List the specific topics you still need to cover (comma-separated or one per line)."
            )

            subject_data[subject] = {
                "chapters_remaining": chapters_remaining,
                "confidence": confidence,
                "topics": topics_remaining
            }

    else:
        st.warning("⚠️ Add at least one subject to continue!")
        subject_data = {}

    st.divider()

    # =========================
    # EXECUTION CAPACITY (FOURTH)
    # =========================

    st.subheader("⚡ Execution Capacity")

    hours = st.slider(
        "Available Study Hours Per Day",
        1.0,
        12.0,
        4.0,
        step=0.5
    )

    burnout = st.selectbox(
        "Current Burnout Level",
        ["Low", "Moderate", "High"]
    )

    consistency = st.selectbox(
        "Consistency Level",
        ["Very Poor", "Average", "Good", "Very Consistent"]
    )

    st.divider()

    # =========================
    # ADDITIONAL CONTEXT (LAST)
    # =========================

    st.subheader("🧠 Additional Context")

    extra_context = st.text_area(
        "Anything else the planner should know?",
        placeholder="""
Example:
- I procrastinate a lot
- I panic before exams
- My college schedule is exhausting
- I struggle with consistency
"""
    )

    st.divider()

    # =========================
    # SUBMIT BUTTON
    # =========================

    submitted = st.form_submit_button(
        "Generate AI Study Plan",
        use_container_width=True
    )

# =========================
# AI RESPONSE
# =========================

if submitted:

    if not st.session_state.subjects_list:
        st.error("❌ Please add at least one subject before generating a plan!")
    else:

        final_exam = custom_exam if exam == "Other" else exam

        with st.spinner("Analyzing your academic situation..."):

            ai_response = generate_study_plan(
                final_exam,
                exam_date,
                exam_format,
                subject_data,
                hours,
                burnout,
                consistency,
                extra_context
            )

        # Save response
        st.session_state.ai_response = ai_response

# Show response only if it exists
if "ai_response" in st.session_state:

    st.success("✅ AI Study Plan Generated")

    st.divider()

    with st.container(border=True):

        st.subheader("📘 Your AI Guidance")

        st.markdown(st.session_state.ai_response)