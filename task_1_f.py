import requests

# Function to fetch and display user data from the JSONPlaceholder API
def fetch_user_data():
    try:
        # Send GET request to the API
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        
        # Check if the request was successful
        if response.status_code == 200:
            users = response.json()  # Parse the JSON response
            
            # Display specific information for each user
            print("User Details:\n")
            for user in users:
                # Display 'Akanksha' as the name
                if user['name'] == 'Leanne Graham':  # Replace this with any other condition if you need
                    print(f"Name: Akanksha")
                else:
                    print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print("-" * 40)
        else:
            print(f"Failed to fetch data from the API. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Call the function to fetch and display user data
fetch_user_data()
