weather_conditions = input("What's the weather like today? (sunny/rainy/cold):")
weather_conditions = weather_conditions.lower().strip()

if weather_conditions == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_conditions == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif weather_conditions == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
