import requests

def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    if response.status_code == 200:
        advice = response.json()["slip"]["advice"]
        return advice
    return "Не удалось получить совет. Попробуйте позже."

def main():
    print("Ваш случайный совет:")
    print(get_advice())

if __name__ == "__main__":
    main()
