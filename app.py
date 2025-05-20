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

# Reset button logic
if st.sidebar.button("Reset Assessment"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
    
# -----------------------------
# Avatar Assessment Questions
# -----------------------------

avatar_questions = [
    ("What brings you the most fulfillment?", {
        "A": ("Disciple Developer", "Helping others grow spiritually or personally."),
        "B": ("Encouraging Connector", "Bringing people together through encouragement."),
        "C": ("Legacy Leader", "Designing something that lasts beyond me."),
        "D": ("Insight Investigator", "Discovering deep truths that others miss.")
    }),
    ("When you have free time, what are you most drawn to?", {
        "A": ("Empowered Creator", "Creating art, writing, or new ideas."),
        "B": ("Architect of Meaning", "Organizing or planning something meaningful."),
        "C": ("Faithful Shepherd", "Spending time with someone in need of comfort."),
        "D": ("Purposeful Pathfinder", "Exploring new places or starting new projects.")
    }),
    ("Which role would you most naturally take in a group project?", {
        "A": ("Integrator", "Ensure the group’s values and actions align."),
        "B": ("Empowered Creator", "Come up with a creative way to tell the story."),
        "C": ("Encouraging Connector", "Keep people energized and connected."),
        "D": ("Insight Investigator", "Quietly observe and offer insights at key moments.")
    }),
    ("Which of these best describes how you approach challenges?", {
        "A": ("Legacy Leader", "Create a thoughtful plan and execute it."),
        "B": ("Faithful Shepherd", "Respond with empathy and presence."),
        "C": ("Purposeful Pathfinder", "Adapt quickly and lead others into the unknown."),
        "D": ("Integrator", "Consider how all parts of life are affected.")
    }),
    ("What motivates you most?", {
        "A": ("Legacy Leader", "Impacting the next generation."),
        "B": ("Faithful Shepherd", "Helping people heal and be whole."),
        "C": ("Liberated Giver", "Giving time, money, or resources freely."),
        "D": ("Architect of Meaning", "Building ideas that serve a greater purpose.")
    }),
    ("Which of these are you most likely to say?", {
        "A": ("Encouraging Connector", "Let’s make this fun and meaningful for everyone."),
        "B": ("Insight Investigator", "We should think through the deeper implications."),
        "C": ("Integrator", "Let’s ensure this decision reflects our values."),
        "D": ("Faithful Shepherd", "Who needs support right now? Let’s be present.")
    }),
    ("When considering your future, what excites you most?", {
        "A": ("Empowered Creator", "Creating something meaningful that serves others."),
        "B": ("Legacy Leader", "Passing on wisdom and resources to others."),
        "C": ("Purposeful Pathfinder", "Going where I’m called, even if it’s unknown."),
        "D": ("Disciple Developer", "Discipling or mentoring others along the way.")
    }),
    ("How do you tend to respond when someone is hurting?", {
        "A": ("Faithful Shepherd", "I sit with them, quietly present."),
        "B": ("Encouraging Connector", "I share encouraging words and build their hope."),
        "C": ("Insight Investigator", "I ask thoughtful questions to help them find clarity."),
        "D": ("Liberated Giver", "I offer what I have — time, money, attention.")
    }),
    ("Which statement best reflects your instinct?", {
        "A": ("Purposeful Pathfinder", "I want to blaze new trails."),
        "B": ("Encouraging Connector", "I want to bring people joy and connection."),
        "C": ("Liberated Giver", "I want to give in ways that transform lives."),
        "D": ("Architect of Meaning", "I want to organize truth for lasting impact.")
    }),
    ("Which of these is your biggest strength?", {
        "A": ("Faithful Shepherd", "Listening deeply and offering emotional presence."),
        "B": ("Empowered Creator", "Creating visual or written expressions that move people."),
        "C": ("Legacy Leader", "Casting vision and leading forward."),
        "D": ("Integrator", "Helping others align their lives with their purpose.")
    }),
    ("What do people often thank you for?", {
        "A": ("Liberated Giver", "Being a generous and supportive presence."),
        "B": ("Disciple Developer", "Helping them grow in faith or clarity."),
        "C": ("Integrator", "Making things work smoothly and with integrity."),
        "D": ("Insight Investigator", "Bringing insight they hadn’t considered.")
    }),
    ("What kind of projects do you enjoy most?", {
        "A": ("Architect of Meaning", "Designing or building something impactful."),
        "B": ("Purposeful Pathfinder", "Stretching into new territory."),
        "C": ("Disciple Developer", "Mentoring or guiding others."),
        "D": ("Empowered Creator", "Creative thinking and expression.")
    })
]

st.header("Part 1: Avatar Discovery")
avatar_scores = {}

for i, (question, options) in enumerate(avatar_questions, 1):
    st.subheader(f"{i}. {question}")
    labels = [f"{key}: {text}" for key, (_, text) in options.items()]
    response = st.radio("", labels, key=f"avatar_q{i}")
    selected_key = response.split(":")[0].strip()
    selected_avatar = options[selected_key][0]
    avatar_scores[selected_avatar] = avatar_scores.get(selected_avatar, 0) + 1

# -----------------------------
# Expression Overlay Assessment
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
    selected_key = response.split(":")[0].strip()
    selected_overlay = options[selected_key][0]
    overlay_scores[selected_overlay] = overlay_scores.get(selected_overlay, 0) + 1
    
# -----------------------------
# Calculate and Display Results
# -----------------------------

if st.button("Calculate My Profile"):
    primary_avatar = max(avatar_scores, key=avatar_scores.get)
    wings = sorted(avatar_scores.items(), key=lambda x: -x[1])
    wing_avatars = [w[0] for w in wings if w[0] != primary_avatar][:2]
    expression_overlay = max(overlay_scores, key=overlay_scores.get)

    st.markdown("---")
    st.header("Your IDEAL LIFE™ Profile")
    st.subheader(f"Primary Avatar: {primary_avatar}")

    st.subheader("Wings:")
    for wing in wing_avatars:
        st.write(f"- {wing}")

    st.subheader(f"Expression Overlay: {expression_overlay}")

    match = df[(df["Primary Avatar"] == primary_avatar) &
               (df["Wing Avatar"].isin(wing_avatars)) &
               (df["Expression Overlay"] == expression_overlay)]

    if not match.empty:
        report = match.iloc[0]
        st.markdown("---")
        st.subheader("Narrative Summary")
        st.write(report["Core Narrative"])
        st.write(report["Wing Description"])
        st.write(report["Overlay Description"])
    else:
        st.warning("A full narrative profile could not be found for this combination.")
