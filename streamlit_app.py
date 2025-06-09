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

# === Helper Functions ===
def generate_metaphor(mood):
    metaphors = {
        "🌞 Joy": [
            "Your wings unfurl in sunlight, radiant and golden.",
            "A songbird builds a nest in the heart of your soul."
        ],
        "🌧️ Sadness": [
            "Your feathers are soaked, but the sky remembers how to clear.",
            "Raindrops trace the lines of your healing scars."
        ],
        "🔥 Anger": [
            "Your wings catch fire, forging light through fury.",
            "A blaze rises within, carving paths in shadowed lands."
        ],
        "🌊 Reflection": [
            "You glide over mirrored lakes, seeking hidden truths.",
            "Depth speaks in silence beneath your wings."
        ],
        "🌈 Hope": [
            "Your glow returns, soft but steady like dawn.",
            "New colors shimmer in places you thought lost."
        ]
    }
    return random.choice(metaphors.get(mood, ["Your journey deepens..."]))

def evolve_creature(mood):
    # Mutate creature stats depending on mood
    if mood == "🌞 Joy" or mood == "🌈 Hope":
        st.session_state.creature_stats["wings"] += 1
        st.session_state.creature_stats["glow"] = "bright"
    elif mood == "🌧️ Sadness" or mood == "🌊 Reflection":
        st.session_state.creature_stats["scars"] += 1
        st.session_state.creature_stats["glow"] = "soft"
    elif mood == "🔥 Anger":
        st.session_state.creature_stats["wings"] += 1
        st.session_state.creature_stats["scars"] += 1
        st.session_state.creature_stats["glow"] = "flickering"

# === Journal Entry Page ===
if view == "📖 Journal Entry":
    st.subheader("New Entry")
    entry = st.text_area("Write about your emotion, memory, or moment:")
    mood = st.selectbox("Select a mood that fits:", ["🌞 Joy", "🌧️ Sadness", "🔥 Anger", "🌊 Reflection", "🌈 Hope"])
    if st.button("Submit Entry") and entry.strip():
        metaphor = generate_metaphor(mood)
        evolve_creature(mood)
        st.session_state.entries.append({
            "text": entry.strip(),
            "mood": mood,
            "metaphor": metaphor
        })
        st.success("Entry saved! Your soul creature has evolved.")
        st.info(f"🌟 {metaphor}")

# === Memory Map Page ===
elif view == "🗺️ Memory Map":
    st.subheader("🗺️ Your Inner Landscape")
    if not st.session_state.entries:
        st.info("No entries yet. Add one to begin your map.")
    for i, e in enumerate(st.session_state.entries):
        st.markdown(f"**Region {i+1} – Mood: {e['mood']}**")
        st.markdown(f"> *{e['metaphor']}*")
        st.caption(f"📜 {e['text']}")
        st.markdown("---")

# === Soul Creature Page ===
elif view == "🦋 Soul Creature":
    st.subheader("🦋 Your Soul Creature")
    st.markdown("This ethereal being mirrors your inner growth.")
    stats = st.session_state.creature_stats
    st.write(f"**Wings:** Level {stats['wings']}")
    st.write(f"**Glow:** {stats['glow'].capitalize()}")
    st.write(f"**Scars:** {stats['scars']} (a record of survival)")

# === Archive Page ===
elif view == "📚 Archive":
    st.subheader("📚 Past Entries")
    if not st.session_state.entries:
        st.info("You have no journal entries yet.")
    for i, e in enumerate(reversed(st.session_state.entries)):
        st.markdown(f"**Day {len(st.session_state.entries)-i} – Mood: {e['mood']}**")
        st.markdown(f"📖 {e['text']}")
        st.caption(f"✨ {e['metaphor']}")
        st.markdown("---")


