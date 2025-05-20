import streamlit as st
import pandas as pd
from collections import Counter

# Load avatar-wing-overlay matrix
@st.cache_data
def load_data():
    df = pd.read_excel("IDEAL_LIFE_Final_Client_Report_Generator.xlsx")
    return df

df = load_data()

st.set_page_config(page_title="IDEAL LIFE Assessment", layout="centered")
st.title("IDEAL LIFE™ Client Assessment")

st.markdown("---")
st.header("Step 1: Avatar Identification")

# Define 12 avatar questions and mapping
avatar_questions = [
    ("What brings you the most fulfillment?", [
        ("Helping others grow spiritually or personally.", "Disciple Developer"),
        ("Bringing people together through encouragement.", "Encouraging Connector"),
        ("Designing something that lasts beyond me.", "Legacy Leader"),
        ("Discovering deep truths that others miss.", "Insight Investigator")
    ]),
    ("When you have free time, what are you most drawn to?", [
        ("Creating art, writing, or new ideas.", "Empowered Creator"),
        ("Organizing or planning something meaningful.", "Architect of Meaning"),
        ("Spending time with someone in need of comfort.", "Faithful Shepherd"),
        ("Exploring new places or starting new projects.", "Purposeful Pathfinder")
    ]),
    ("Which role would you most naturally take in a group project?", [
        ("Ensure the group’s values and actions align.", "Integrator"),
        ("Come up with a creative way to tell the story.", "Empowered Creator"),
        ("Keep people energized and connected.", "Encouraging Connector"),
        ("Quietly observe and offer insights at key moments.", "Insight Investigator")
    ]),
    ("Which of these best describes how you approach challenges?", [
        ("Create a thoughtful plan and execute it.", "Legacy Leader"),
        ("Respond with empathy and presence.", "Faithful Shepherd"),
        ("Adapt quickly and lead others into the unknown.", "Purposeful Pathfinder"),
        ("Consider how all parts of life are affected.", "Integrator")
    ]),
    ("What motivates you most?", [
        ("Impacting the next generation.", "Legacy Leader"),
        ("Helping people heal and be whole.", "Faithful Shepherd"),
        ("Giving time, money, or resources freely.", "Liberated Giver"),
        ("Building ideas that serve a greater purpose.", "Architect of Meaning")
    ]),
    ("Which of these are you most likely to say?", [
        ("Let’s make this fun and meaningful for everyone.", "Encouraging Connector"),
        ("We should think through the deeper implications.", "Insight Investigator"),
        ("Let’s ensure this decision reflects our values.", "Integrator"),
        ("Who needs support right now? Let’s be present.", "Faithful Shepherd")
    ]),
    ("When considering your future, what excites you most?", [
        ("Creating something meaningful that serves others.", "Empowered Creator"),
        ("Passing on wisdom and resources to others.", "Legacy Leader"),
        ("Going where I’m called, even if it’s unknown.", "Purposeful Pathfinder"),
        ("Discipling or mentoring others along the way.", "Disciple Developer")
    ]),
    ("How do you tend to respond when someone is hurting?", [
        ("I sit with them, quietly present.", "Faithful Shepherd"),
        ("I share encouraging words and build their hope.", "Encouraging Connector"),
        ("I ask thoughtful questions to help them find clarity.", "Insight Investigator"),
        ("I offer what I have — time, money, attention.", "Liberated Giver")
    ]),
    ("Which statement best reflects your instinct?", [
        ("I want to blaze new trails.", "Purposeful Pathfinder"),
        ("I want to bring people joy and connection.", "Encouraging Connector"),
        ("I want to give in ways that transform lives.", "Liberated Giver"),
        ("I want to organize truth for lasting impact.", "Architect of Meaning")
    ]),
    ("Which of these is your biggest strength?", [
        ("Listening deeply and offering emotional presence.", "Faithful Shepherd"),
        ("Creating visual or written expressions that move people.", "Empowered Creator"),
        ("Casting vision and leading forward.", "Legacy Leader"),
        ("Helping others align their lives with their purpose.", "Integrator")
    ]),
    ("What do people often thank you for?", [
        ("Being a generous and supportive presence.", "Liberated Giver"),
        ("Helping them grow in faith or clarity.", "Disciple Developer"),
        ("Making things work smoothly and with integrity.", "Integrator"),
        ("Bringing insight they hadn’t considered.", "Insight Investigator")
    ]),
    ("What kind of projects do you enjoy most?", [
        ("Ones that involve designing or building something impactful.", "Architect of Meaning"),
        ("Ones that stretch me into new territory.", "Purposeful Pathfinder"),
        ("Ones that involve mentoring or guiding others.", "Disciple Developer"),
        ("Ones that require beauty, design, or creative thinking.", "Empowered Creator")
    ])
]

responses = []
for i, (question, options) in enumerate(avatar_questions):
    st.subheader(f"Q{i+1}. {question}")
    choice = st.radio("", [opt[0] for opt in options], key=f"q{i}")
    for label, avatar in options:
        if choice == label:
            responses.append(avatar)
            break

if st.button("Calculate Avatar Results"):
    avatar_count = Counter(responses)
    primary_avatar, *_ = avatar_count.most_common(1)
    wings = [a for a, _ in avatar_count.most_common()[1:3]]

    st.success(f"Primary Avatar: {primary_avatar}")
    st.info(f"Wings: {', '.join(wings)}")
    st.session_state["primary_avatar"] = primary_avatar
    st.session_state["wings"] = wings
    st.session_state["avatar_selected"] = True

if st.session_state.get("avatar_selected"):
    st.markdown("---")
    st.header("Step 2: Expression Overlay Assessment")
    st.markdown("Now we're going to explore how you live out your primary calling.")

    overlay_questions = [
    ("When you're at your best, what are you doing?", {
        "A. Casting vision and motivating others.": "Visionary Strategist",
        "B. Helping someone feel seen, heard, or cared for.": "Relational Nurturer",
        "C. Creating something new with my hands or ideas.": "Creative Builder",
        "D. Solving problems quietly and practically.": "Grounded Executor",
        "E. Thinking deeply and synthesizing ideas.": "Reflective Thinker",
        "F. Lifting others’ spirits and bringing positive energy.": "Joyful Connector"
    }),
    ("What part of your work gives you the most energy?", {
        "A. Sharing big ideas and seeing others inspired.": "Visionary Strategist",
        "B. Being present with someone in a meaningful moment.": "Relational Nurturer",
        "C. Building something beautiful, useful, or expressive.": "Creative Builder",
        "D. Making sure everything gets done the right way.": "Grounded Executor",
        "E. Time alone to think, reflect, or journal.": "Reflective Thinker",
        "F. Connecting with people and encouraging them.": "Joyful Connector"
    }),
    ("Which compliment would you most like to receive?", {
        "A. You have a gift for rallying people toward what matters.": "Visionary Strategist",
        "B. You make people feel truly cared for.": "Relational Nurturer",
        "C. You have such a creative and unique way of expressing things.": "Creative Builder",
        "D. You’re dependable, detailed, and organized.": "Grounded Executor",
        "E. You always offer deep insight or ask the perfect question.": "Reflective Thinker",
        "F. You brighten every room you enter.": "Joyful Connector"
    }),
    ("What’s your favorite way to contribute to a team?", {
        "A. Lead with vision and clarity.": "Visionary Strategist",
        "B. Offer care and emotional support.": "Relational Nurturer",
        "C. Bring creative ideas and original thinking.": "Creative Builder",
        "D. Handle the logistics and make it work.": "Grounded Executor",
        "E. Clarify the deeper purpose or structure.": "Reflective Thinker",
        "F. Keep energy high and people connected.": "Joyful Connector"
    }),
    ("What brings you the most joy?", {
        "A. Launching a new vision or project.": "Visionary Strategist",
        "B. Helping someone heal or feel safe.": "Relational Nurturer",
        "C. Creating or designing something beautiful.": "Creative Builder",
        "D. Checking off a task list or completing something well.": "Grounded Executor",
        "E. Seeing a pattern or insight no one else noticed.": "Reflective Thinker",
        "F. Laughing and celebrating with people.": "Joyful Connector"
    })
]

    overlay_responses = []
    for i, (question, options) in enumerate(overlay_questions):
        st.subheader(f"Overlay Q{i+1}. {question}")
        choice = st.radio("Choose the option that best fits you:", list(options.keys()), key=f"overlay_q{i}")
        overlay_responses.append(options[choice])

    if st.button("Calculate Expression Overlay"):
    overlay_count = Counter(overlay_responses)
    top_overlay = overlay_count.most_common(1)[0][0]
    st.session_state["overlay"] = top_overlay
    st.session_state["overlay_calculated"] = True

    # Load description data from the report generator file
    result = df[
        (df["Primary Avatar"] == st.session_state["primary_avatar"]) &
        (df["Wing Avatar"].isin(st.session_state["wings"])) &
        (df["Expression Overlay"] == top_overlay)
    ].head(1)

    if not result.empty:
        row = result.iloc[0]
        st.markdown("---")
        st.header("Final Client Narrative Summary")

        st.subheader(f"Primary Avatar: {row['Primary Avatar']}")
        st.write(row["Core Narrative"])

        st.subheader(f"Wing Avatar: {row['Wing Avatar']}")
        st.write(row["Wing Description"])

        st.subheader(f"Expression Overlay: {row['Expression Overlay']}")
        overlay_narratives = {
    "Visionary Strategist": "You live out your calling as a Visionary Strategist — someone who casts bold vision and moves others toward meaningful outcomes. This means you tend to lead with clarity, pursue long-term goals, and inspire aligned action. Others experience you as forward-focused and mission-driven. When aligned, your style brings direction and momentum; when misaligned, it may manifest as over-control or burnout.",
    "Relational Nurturer": "You live out your calling as a Relational Nurturer — someone who creates safety, trust, and care in your relationships. This means you tend to serve through empathy, attentiveness, and emotional support. Others experience you as a grounded and faithful presence. When aligned, your style fosters healing and belonging; when misaligned, it may show up as over-identification with others’ emotions or exhaustion.",
    "Creative Builder": "You live out your calling as a Creative Builder — someone who brings truth and beauty to life through tangible expression. This means you are often creating, shaping, or designing things that reflect deeper values. Others experience you as inventive and inspirational. When aligned, your work invites others into wonder and insight; when misaligned, you may feel misunderstood, unproductive, or overly idealistic.",
    "Grounded Executor": "You live out your calling as a Grounded Executor — someone who thrives on structure, discipline, and dependable contribution. This means you turn ideas into reality with consistency and excellence. Others experience you as reliable, practical, and trustworthy. When aligned, your presence builds confidence and traction; when misaligned, it may become rigid, perfectionistic, or resistant to change.",
    "Reflective Thinker": "You live out your calling as a Reflective Thinker — someone who processes deeply and distills clarity from complexity. This means you need time, space, and solitude to develop meaningful insight. Others experience you as thoughtful, wise, and discerning. When aligned, your style reveals truth and direction; when misaligned, it may appear withdrawn, overly analytical, or disconnected.",
    "Joyful Connector": "You live out your calling as a Joyful Connector — someone who energizes others and infuses environments with warmth. This means you share your purpose through presence, affirmation, and community. Others experience you as uplifting, lively, and contagious in your enthusiasm. When aligned, your style brings life and encouragement; when misaligned, it may show up as scattered focus or avoidance of depth."
}
overlay_description = overlay_narratives.get(row['Expression Overlay'], row['Overlay Description'])
        st.write(overlay_description)
    else:
        st.warning("No complete narrative match found for this combination. Please verify the dataset.")
