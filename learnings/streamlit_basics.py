import streamlit as st


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Streamlit Basics",
    page_icon="🚀",
    layout="wide"
)


# ==============================
# TITLES & TEXT
# ==============================

st.title("🚀 Streamlit Basics")

st.header("This is a Header")

st.subheader("This is a Subheader")

st.text("This is simple text")

st.markdown("""
### Markdown Support

You can write:
- bullet points
- headings
- bold text
- multiline content
""")


# ==============================
# DIVIDER
# ==============================

st.divider()


# ==============================
# BUTTONS
# ==============================

st.header("Buttons")

if st.button("Click Me"):
    st.success("Button Clicked!")


# ==============================
# COLUMNS
# ==============================

st.divider()

st.header("Columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("Column 1")

with col2:
    st.warning("Column 2")

with col3:
    st.error("Column 3")


# ==============================
# METRICS
# ==============================

st.divider()

st.header("Metrics")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("DSA Questions", "12")

with m2:
    st.metric("Focus Hours", "5 hrs")

with m3:
    st.metric("Burnout Risk", "Low")


# ==============================
# INPUT FIELDS
# ==============================

st.divider()

st.header("Inputs")

name = st.text_input("Enter Your Name")

study_hours = st.slider(
    "Study Hours",
    1,
    12,
    4
)

subject = st.selectbox(
    "Favorite Subject",
    ["Physics", "Chemistry", "Maths", "DSA"]
)

subjects = st.multiselect(
    "Subjects You Study",
    ["Physics", "Chemistry", "Maths", "DSA"]
)

days = st.number_input(
    "Days Left for Exam",
    1,
    365,
    30
)


# ==============================
# FORM
# ==============================

st.divider()

st.header("Form Example")

with st.form("sample_form"):

    exam = st.text_input("Exam Name")

    confidence = st.selectbox(
        "Confidence Level",
        ["Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Submit Form")

if submitted:

    st.success("Form Submitted!")

    st.write(f"Exam: {exam}")
    st.write(f"Confidence: {confidence}")


# ==============================
# SESSION STATE
# ==============================

st.divider()

st.header("Session State")

if st.button("Save Name"):

    st.session_state.saved_name = name

if "saved_name" in st.session_state:

    st.success(
        f"Saved Name: {st.session_state.saved_name}"
    )


# ==============================
# CONDITIONAL LOGIC
# ==============================

st.divider()

st.header("Conditional Logic")

if study_hours >= 8:

    st.success("Excellent consistency.")

elif study_hours >= 5:

    st.warning("Good, but can improve.")

else:

    st.error("Very low study hours.")