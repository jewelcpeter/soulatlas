# 🦋 Mythoscape – MVP Streamlit Layout

import streamlit as st
import random

st.set_page_config(page_title="🦋 Mythoscape", layout="wide")
st.title("🦋 Mythoscape")
st.caption("A self-growth journal where your soul creature evolves and memories shape your inner world.")

# === Sidebar for Navigation ===
st.sidebar.title("Navigate")
view = st.sidebar.radio("Go to:", ["📖 Journal Entry", "🗺️ Memory Map", "🦋 Soul Creature", "📚 Archive"])

# === Storage (for MVP, just session) ===
if "entries" not in st.session_state:
    st.session_state.entries = []
if "creature_stats" not in st.session_state:
    st.session_state.creature_stats = {"wings": 1, "glow": "dim", "scars": 0}

# === Journal Entry Page ===
if view == "📖 Journal Entry":
    st.subheader("New Entry")
    entry = st.text_area("Write about your emotion, memory, or moment:")
    mood = st.selectbox("Select a mood that fits:", ["🌞 Joy", "🌧️ Sadness", "🔥 Anger", "🌊 Reflection", "🌈 Hope"])
    if st.button("Submit Entry"):
        # Fake metaphor + creature evolution
        metaphor = random.choice([
            "Your wings shimmer with quiet resilience.",
            "A storm brews in the valley of your past.",
            "Your glow softens, but grows ever wider.",
            "Roots twist beneath the mountain of memory."
        ])
        st.session_state.entries.append({"text": entry, "mood": mood, "metaphor": metaphor})
        st.success("Entry saved! Your soul creature has evolved.")

# === Memory Map Page ===
elif view == "🗺️ Memory Map":
    st.subheader("Your Inner Landscape")
    for i, e in enumerate(st.session_state.entries):
        st.markdown(f"**Region {i+1}** – *{e['mood']}*\n> {e['metaphor']}")
        st.caption(e['text'])
        st.markdown("---")

# === Soul Creature Page ===
elif view == "🦋 Soul Creature":
    st.subheader("Your Soul Creature")
    st.write("Visuals coming soon – for now, here's a description:")
    st.write("- Wings: Level", st.session_state.creature_stats['wings'])
    st.write("- Glow: ", st.session_state.creature_stats['glow'])
    st.write("- Scars: ", st.session_state.creature_stats['scars'])

# === Archive Page ===
elif view == "📚 Archive":
    st.subheader("Past Entries")
    for i, e in enumerate(reversed(st.session_state.entries)):
        st.markdown(f"**Day {len(st.session_state.entries)-i}** – {e['mood']}\n> {e['text']}")
        st.caption(e['metaphor'])
        st.markdown("---")

