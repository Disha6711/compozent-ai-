import requests

def fetch_user_data():
    try:
        
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        
        if response.status_code == 200:
            users = response.json()  
            
            print("User Details:\n")
            for user in users:
                
                if user['name'] == 'Leanne Graham':  
                    print(f"Name: Disha Gareja")
                else:
                    print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print("-" * 40)
        else:
            print(f"Failed to fetch data from the API. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

fetch_user_data()
