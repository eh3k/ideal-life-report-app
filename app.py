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

avatar_questions = [
    # The full avatar questions will go here — already provided in previous version.
]

st.header("Part 1: Avatar Discovery")
avatar_scores = {}

for i, (question, options) in enumerate(avatar_questions, 1):
    st.subheader(f"{i}. {question}")
    labels = [f"{key}: {text}" for key, (_, text) in options.items()]
    response = st.radio("", labels, key=f"avatar_q{i}")
    selected_key = response.split(":")[0]
    selected_avatar = options[selected_key][0]
    avatar_scores[selected_avatar] = avatar_scores.get(selected_avatar, 0) + 1

# -----------------------------
# Expression Overlay Assessment
# -----------------------------

overlay_questions = [
    # The full overlay questions will go here — already provided in previous version.
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

    # Lookup full narrative report if available
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
