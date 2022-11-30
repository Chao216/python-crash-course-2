# while break 案例

prompt = "\nplease enter a city you love most."

prompt += "\nEnter 'quit' to end this program."


while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"\nI would like to visit {city.title()} one day !")
