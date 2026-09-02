import streamlit as st
import google.generativeai as genai



api_key = st.secrets.get("GEMINI_API_KEY", None)

st.set_page_config(page_title="AI Fitness & Diet Planner", page_icon="💪", layout="wide")

with st.sidebar:
    st.header("💪 Your Profile")
    st.divider()
    if api_key:
        st.success("API Key loaded")
    else:
        api_key = st.text_input("API Key", type="password")
    st.divider()
    age = st.number_input("Age", 14, 65, 21)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", 30, 200, 68)
    height = st.number_input("Height (cm)", 120, 220, 170)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Fit", "Improve Stamina", "Flexibility"])
    activity = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
    location = st.selectbox("Workout Location", ["Home (no equipment)", "Home (dumbbells, bands)", "College Gym", "Full Gym"])
    time_available = st.selectbox("Time Per Day", ["15-20 min", "30-40 min", "45-60 min", "60+ min"])
    diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Eggetarian"])
    cuisine = st.selectbox("Food Preference", ["South Indian", "North Indian", "Indian Mixed", "Mediterranean", "Western"])
    budget = st.selectbox("Food Budget", ["Low (student)", "Moderate", "Flexible"])
    currency = st.selectbox("Currency", ["INR", "USD", "EUR", "GBP"])
    health = st.text_input("Health Conditions (optional)", placeholder="e.g. Knee injury")
    if not health:
        health = "None"

st.title("💪 AI Fitness & Diet Planner")
st.write("Personalized workout routines & meal plans powered by Gemini AI")
st.divider()

generate = st.button("🚀 Generate My Plan", use_container_width=True)

if generate:
    if not api_key:
        st.error("Please add GEMINI_API_KEY in .env file or enter in sidebar.")
    else:
        st.info(
            f"*{gender}, {age} yrs* | {weight}kg | {height}cm | "
            f"*Goal:* {goal} | *Diet:* {diet} | *Cuisine:* {cuisine}"
        )
        prompt = f"""You are an expert fitness trainer and nutritionist for college students.
Create a personalized plan for:
Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm
Goal: {goal}, Activity: {activity}, Location: {location}, Time: {time_available}
Diet: {diet}, Cuisine: {cuisine}, Budget: {budget} ({currency}), Health: {health}

Generate:
1. WEEKLY WORKOUT PLAN (Mon-Sun) with exercises, sets, reps for their equipment
2. DAILY MEAL PLAN (Breakfast, Snack, Lunch, Snack, Dinner) using {cuisine} foods, budget-friendly, with calories and protein
3. 4 PRACTICAL TIPS

Use markdown headers, tables, and bullet points."""

        with st.spinner("Generating your personalized plan..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-3.6-flash")
                response = model.generate_content(prompt)
                result = response.text
                if result:
                    st.divider()
                    st.subheader("Your Personalized Plan")
                    st.markdown(result)
                    st.divider()
                    st.download_button("Download Plan", result, "my_fitness_plan.md", use_container_width=True)
                else:
                    st.error("AI returned empty response. Try again.")
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.markdown("### How to use\n1. Enter details in the *sidebar\n2. Click **Generate My Plan*\n3. Your plan appears here")