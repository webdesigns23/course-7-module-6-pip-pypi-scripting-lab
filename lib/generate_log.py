from datetime import datetime
import requests

def generate_log(data):
    if isinstance(data, list):
        log_data = data
    else:
        raise ValueError("Error, Log data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename

# def fetch_data():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts")
#     if response.status_code == 200:
#         return response.json()
#     return {}

# if __name__ == "__main__":
#     posts = fetch_data()
#     data = []
#     for post in posts:
#         data.append(post.get("title"))
#     generate_log(data)