import streamlit as st
import pandas as pd

# Load report narrative data
@st.cache_data
def load_data():
    df = pd.read_excel("IDEAL_LIFE_Final_Client_Report_Generator.xlsx")
    return df

df = load_data()

st.set_page_config(page_title="IDEAL LIFE Assessment", layout="centered")
st.title("IDEAL LIFE™ Discovery Assessment")
st.markdown("Answer the following questions to discover your Avatar, Wings, and Expression Overlay.")

# -----------------------------
# Avatar Assessment Questions
# -----------------------------

# (avatar_questions block remains unchanged)

# (avatar scoring block remains unchanged)

# -----------------------------
# Correct Overlay Assessment Questions
# -----------------------------

overlay_questions = [
    ("When you're at your best, what are you doing?", {
        "A": ("Visionary Strategist", "Casting vision and motivating others."),
        "B": ("Relational Nurturer", "Helping someone feel seen, heard, or cared for."),
        "C": ("Creative Builder", "Creating something new with my hands or ideas."),
        "D": ("Grounded Executor", "Solving problems quietly and practically."),
        "E": ("Reflective Thinker", "Thinking deeply and synthesizing ideas."),
        "F": ("Joyful Connector", "Lifting others’ spirits and bringing positive energy.")
    }),
    ("What part of your work gives you the most energy?", {
        "A": ("Visionary Strategist", "Sharing big ideas and seeing others inspired."),
        "B": ("Relational Nurturer", "Being present with someone in a meaningful moment."),
        "C": ("Creative Builder", "Building something beautiful, useful, or expressive."),
        "D": ("Grounded Executor", "Making sure everything gets done the right way."),
        "E": ("Reflective Thinker", "Time alone to think, reflect, or journal."),
        "F": ("Joyful Connector", "Connecting with people and encouraging them.")
    }),
    ("Which compliment would you most like to receive?", {
        "A": ("Visionary Strategist", "You have a gift for rallying people toward what matters."),
        "B": ("Relational Nurturer", "You make people feel truly cared for."),
        "C": ("Creative Builder", "You have such a creative and unique way of expressing things."),
        "D": ("Grounded Executor", "You’re dependable, detailed, and organized."),
        "E": ("Reflective Thinker", "You always offer deep insight or ask the perfect question."),
        "F": ("Joyful Connector", "You brighten every room you enter.")
    }),
    ("What’s your favorite way to contribute to a team?", {
        "A": ("Visionary Strategist", "Lead with vision and clarity."),
        "B": ("Relational Nurturer", "Offer care and emotional support."),
        "C": ("Creative Builder", "Bring creative ideas and original thinking."),
        "D": ("Grounded Executor", "Handle the logistics and make it work."),
        "E": ("Reflective Thinker", "Clarify the deeper purpose or structure."),
        "F": ("Joyful Connector", "Keep energy high and people connected.")
    }),
    ("What brings you the most joy?", {
        "A": ("Visionary Strategist", "Launching a new vision or project."),
        "B": ("Relational Nurturer", "Helping someone heal or feel safe."),
        "C": ("Creative Builder", "Creating or designing something beautiful."),
        "D": ("Grounded Executor", "Checking off a task list or completing something well."),
        "E": ("Reflective Thinker", "Seeing a pattern or insight no one else noticed."),
        "F": ("Joyful Connector", "Laughing and celebrating with people.")
    })
]

st.header("Part 2: Expression Overlay")
overlay_scores = {}

for i, (question, options) in enumerate(overlay_questions, 1):
    st.subheader(f"{i}. {question}")
    labels = [f"{key}: {desc}" for key, (_, desc) in options.items()]
    response = st.radio("", labels, key=f"overlay_q{i}")
    selected_key = response.split(":")[0]
    selected_overlay = options[selected_key][0]
    overlay_scores[selected_overlay] = overlay_scores.get(selected_overlay, 0) + 1
