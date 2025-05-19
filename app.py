import streamlit as st
import pandas as pd

# Load data files
@st.cache_data
def load_data():
    df = pd.read_excel("IDEAL_LIFE_Final_Client_Report_Generator.xlsx")
    return df

df = load_data()

st.set_page_config(page_title="IDEAL LIFE Client Report", layout="centered")
st.title("IDEAL LIFE™ Client Report Generator")
st.markdown("Generate a personalized narrative summary by selecting a primary avatar, wing, and overlay.")

# Dropdown inputs
primary_options = df["Primary Avatar"].unique()
primary_avatar = st.selectbox("Select Primary Avatar", sorted(primary_options))

wing_options = df[df["Primary Avatar"] == primary_avatar]["Wing Avatar"].unique()
wing_avatar = st.selectbox("Select Wing Avatar", sorted(wing_options))

overlay_options = df[(df["Primary Avatar"] == primary_avatar) & (df["Wing Avatar"] == wing_avatar)]["Expression Overlay"].unique()
expression_overlay = st.selectbox("Select Expression Overlay", sorted(overlay_options))

# Filter for the selected combination
record = df[(df["Primary Avatar"] == primary_avatar) &
            (df["Wing Avatar"] == wing_avatar) &
            (df["Expression Overlay"] == expression_overlay)].iloc[0]

# Display Report
st.markdown("---")
st.header("Client Profile Report")

st.subheader(f"Primary Avatar: {primary_avatar}")
st.write(record["Core Narrative"])

st.subheader(f"Wing Avatar: {wing_avatar}")
st.write(record["Wing Description"])

st.subheader(f"Expression Overlay: {expression_overlay}")
st.write(record["Overlay Description"])

# Optional: Personal note
client_note = st.text_area("Add a personal note or advisor observation (optional):")

# Combine full report for copying or export
full_report = f"""
IDEAL LIFE™ Client Report

Primary Avatar: {primary_avatar}
{record['Core Narrative']}

Wing Avatar: {wing_avatar}
{record['Wing Description']}

Expression Overlay: {expression_overlay}
{record['Overlay Description']}

Advisor Note: {client_note if client_note else '(None)'}
"""

st.markdown("---")
if st.button("Copy Full Report"):
    st.code(full_report)
    st.success("Report copied. Paste it into your CRM or document.")

# Future enhancement: PDF export (if desired)
# Requires third-party libraries like `fpdf` or `reportlab`

st.markdown("---")
st.caption("IDEAL LIFE™ Assessment Tool by EverSource")
