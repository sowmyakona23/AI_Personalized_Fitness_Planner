# 💪 AI Fitness & Diet Planner

An AI-powered fitness and diet planning application that generates **personalized workout routines and meal plans** based on an individual's fitness goals, activity level, available workout resources, food preferences, budget, and lifestyle.

The application is built using **Python, Streamlit, and Google Gemini AI**.

---

## 📌 Problem Statement

Most fitness applications provide generic workout and diet plans that do not consider individual needs.

Students and young adults may have different:

* Fitness goals
* Activity levels
* Available workout equipment
* Time availability
* Food preferences
* Cultural food habits
* Dietary requirements
* Food budgets

This project addresses this problem by using **Generative AI to create personalized fitness and nutrition plans** based on user-provided information.

---

## 💡 Proposed Solution

The **AI Fitness & Diet Planner** collects a user's inputs and preferences through an interactive Streamlit interface.

The application sends these details to the **Google Gemini AI model**, which generates:

1. 🏋️ Weekly personalized workout plan
2. 🍽️ Daily personalized meal plan
3. 💡 Practical fitness and lifestyle tips

The generated plan is displayed directly in the application and can also be downloaded as a Markdown file.

---

## ✨ Features

### 👤 Personalized User Profile

Users can provide:

* Age
* Gender
* Weight
* Height
* Fitness Goal
* Activity Level
* Workout Location
* Available Workout Time
* Diet Preference
* Food/Cuisine Preference
* Food Budget
* Currency
* Optional Health Conditions

### 🏋️ Personalized Workout Plan

The AI generates a **Monday–Sunday workout schedule** based on:

* Fitness goal
* Activity level
* Available workout time
* Workout location
* Available equipment

The workout plan includes:

* Exercises
* Sets
* Repetitions
* Weekly schedule

### 🍽️ Personalized Diet Plan

The application generates a daily meal plan containing:

* Breakfast
* Morning/Evening snacks
* Lunch
* Dinner
* Calories
* Protein
* Cuisine-specific food suggestions

The plan considers the user's selected:

* Diet preference
* Cuisine
* Food budget
* Fitness goal

### 💡 Practical Tips

The AI also provides practical fitness and lifestyle recommendations.

### 📥 Download Plan

Users can download their generated plan as a Markdown (`.md`) file.

---

## 🏗️ Application Flow

```text
                ┌───────────────────────┐
                │      User Profile     │
                │                       │
                │ Age, Weight, Height   │
                │ Goal, Activity        │
                │ Diet, Cuisine         │
                │ Budget, Equipment     │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │    Streamlit App      │
                │       (Python)        │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │     Gemini AI Model   │
                │                       │
                │ Personalized Prompt   │
                └───────────┬───────────┘
                            │
                            ▼
             ┌──────────────────────────────┐
             │      Generated AI Plan       │
             │                              │
             │ 🏋️ Weekly Workout Plan       │
             │ 🍽️ Daily Meal Plan           │
             │ 💡 Practical Tips             │
             └──────────────┬───────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Display in UI       │
                │   + Download Plan     │
                └───────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology          | Purpose                       |
| ------------------- | ----------------------------- |
| Python              | Application development       |
| Streamlit           | Web application UI            |
| Google Gemini AI    | Generating personalized plans |
| google-generativeai | Gemini API integration        |
| Markdown            | Formatting generated plans    |

---

## 📂 Project Structure

```text
AI-Fitness-Diet-Planner/
│
├── app.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sowmyakona23/AI_Personalized_Fitness_Planner.git
```

Navigate to the project directory:

```bash
cd AI_Personalized_Fitness_Planner
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key Configuration

The application requires a **Google Gemini API key**.

You can create an API key through Google AI Studio.

For local development, create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

### ⚠️ Security

**Do not upload your API key to GitHub.**

Add the following to `.gitignore`:

```text
.streamlit/secrets.toml
.env
venv/
__pycache__/
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ How to Use

### Step 1 — Enter Profile Information

Use the sidebar to provide:

* Age
* Gender
* Weight
* Height
* Fitness goal
* Activity level
* Workout location
* Workout duration
* Diet preference
* Cuisine preference
* Food budget

### Step 2 — Generate Plan

Click:

**🚀 Generate My Plan**

### Step 3 — AI Generates Your Plan

Gemini AI processes the user's information and generates:

**🏋️ Weekly Workout Plan**

**🍽️ Daily Meal Plan**

**💡 Practical Tips**

### Step 4 — Download

Click:

**Download Plan**

to save the generated plan as a Markdown file.

---

## 🤖 Generative AI Implementation

The application dynamically creates a prompt using the information provided by the user.

Example:

```text
Age: 21
Gender: Male
Weight: 68kg
Height: 170cm
Goal: Muscle Gain
Activity: Moderately Active
Location: College Gym
Time: 45-60 min
Diet: Non-Vegetarian
Cuisine: South Indian
Budget: Moderate
```

These details are passed to Gemini AI with instructions to generate a personalized workout and meal plan.

The AI response is then rendered in the Streamlit application using Markdown formatting.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Build a simple Generative AI application
* Demonstrate prompt engineering
* Generate personalized recommendations using AI
* Consider cultural food preferences
* Consider student-friendly budgets
* Consider available workout resources
* Provide an easy-to-use interface
* Demonstrate AI integration with Python

---

## 🚀 Future Enhancements

The project can be extended with:

* 📈 Progress tracking
* 💾 Save user profiles
* 📅 Workout calendar
* 🥗 More regional cuisines
* 🛒 Automated grocery list
* 📱 Mobile application
* 🧠 AI-based progress analysis
* 🔄 Weekly plan regeneration
* 📊 Fitness progress dashboards

---

## ⚠️ Disclaimer

This application provides **AI-generated fitness and nutrition suggestions for educational and informational purposes only**.

The recommendations should not be considered professional medical, nutritional, or fitness advice.

Users with medical conditions, injuries, allergies, or specific dietary requirements should consult a qualified healthcare professional before following a workout or diet plan.

---

## 👨‍💻 Project

**Project Name:** AI Fitness & Diet Planner

**Category:** Generative AI / AI Application

**Built With:** Python + Streamlit + Google Gemini AI

**Purpose:** Internship / Academic GenAI Project

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
