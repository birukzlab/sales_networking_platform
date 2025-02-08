import requests
import pandas as pd

def fetch_random_users(n=10):
    url = f"https://randomuser.me/api/?results={10}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        users = data.get('results', [])
        df = pd.DataFrame([{'first_name': user['name']['first'],
                            'last_name': user['name']['last'],
                            'email': user['email']
        } for user in users])
        print(df.head())
    else:
            response.raise_for_status()





