# A simple AI agent that decides if it's safe to trek based on conditions
# This is a basic 'Expert System' logic

def trekking_ai_agent(weather, terrain_difficulty):
    if weather == "Sunny" and terrain_difficulty < 7:
        return "Safe to trek. AI recommends proceeding."
    elif weather == "Rainy":
        return "Danger: Slippery terrain. AI recommends staying in camp."
    else:
        return "AI Analysis: Conditions uncertain. Exercise caution."

# Testing our AI Agent
print("--- AI Trekking Assistant ---")
print(trekking_ai_agent("Sunny", 5))