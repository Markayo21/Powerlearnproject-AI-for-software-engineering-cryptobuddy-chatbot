# Step 1: Chatbot Personality
bot_name = "CryptoBuddy"  # The name of the chatbot

# Step 2: Greeting
bot_greeting = "Hey there! I’m CryptoBuddy, your AI-powered crypto sidekick! 🚀"
print(f"{bot_name}: {bot_greeting}")  # Display greeting message when the bot starts

# Step 3: Predefined crypto dataset (acts as a mini database for the chatbot)
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",            # The coin's price movement
        "market_cap": "high",               # The size of the coin's market
        "energy_use": "high",               # How much energy it uses
        "sustainability_score": 3           # Environmental sustainability score (1-10)
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 8
    },
    "Cardano": {
        "price_trend": "trending up",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 6
    }
}

# Step 4: Start continuous user interaction loop
while True:
    user_query = input("\nYou: ").lower()  # Convert user input to lowercase for easy matching

    # Exit the chatbot if the user types 'exit'
    if user_query == "exit":
        print(f"{bot_name}: Remember, crypto investments are risky. Always do your own research! 📢")
        print(f"{bot_name}: Goodbye! Happy crypto investing! 👋")
        break

    # Check for profitability or best buy queries
    elif "profitability" in user_query or "best buy" in user_query:
        # Look for coins that are rising and have high market cap
        profitable_coins = [coin for coin, data in crypto_db.items() 
                            if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable_coins:
            print(f"{bot_name}: For profitability, consider {profitable_coins[0]} — it's trending up with a strong market cap! 💰")
        else:
            print(f"{bot_name}: No top profitable coins right now, but Cardano is a great sustainable option!")

    # Check for sustainability-related queries
    elif "sustainability" in user_query or "eco-friendly" in user_query or "green" in user_query:
        # Return coins that use low energy and have high sustainability score
        sustainable_coins = [coin for coin, data in crypto_db.items()
                             if data["energy_use"] == "low" and data["sustainability_score"] > 7]
        if sustainable_coins:
            print(f"{bot_name}: {', '.join(sustainable_coins)} are eco-friendly coins with good sustainability scores! 🌱")
        else:
            print(f"{bot_name}: Sorry, no highly sustainable coins found currently.")

    # Check for coins trending upward
    elif "trending up" in user_query or "rising" in user_query:
        # List coins with price_trend = "rising"
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            print(f"{bot_name}: These coins are trending up: {', '.join(trending_coins)} 🚀")
        else:
            print(f"{bot_name}: Sorry, I couldn't find any coins trending up right now.")

    # Find the most sustainable coin based on highest sustainability_score
    elif "most sustainable" in user_query or "eco-friendly" in user_query or "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"{bot_name}: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    # Look for long-term growth or future potential queries
    elif "future potential" in user_query or "growth prospects" in user_query:
        # Find coins that are rising and have high market cap
        options = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if options:
            print(f"{bot_name}: {options[0]} is trending up and has a high market cap for long-term growth! 🚀")
        else:
            print(f"{bot_name}: No coins perfectly match your criteria, but Cardano is a solid choice for sustainability and growth!")

    # Catch-all response for unrecognized queries
    else:
        print(f"{bot_name}: Sorry, I didn't understand that. Try asking about trending or sustainable coins, or type 'exit' to quit.")



