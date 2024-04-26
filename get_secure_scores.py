import requests

def get_secure_scores(resource_id):
    # Replace with your actual API endpoint
    api_url = "https://graph.microsoft.com/v1.0/secure-scores"

    # Set up authentication (OAuth2 token)
    # You'll need to handle token acquisition based on your authentication flow
    access_token = "YOUR_ACCESS_TOKEN"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    params = {
        "resourceId": resource_id
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response_data = response.json()

        if response.status_code == 200:
            secure_scores = response_data.get("value", [])
            for score in secure_scores:
                print(f"Resource ID: {score.get('resourceId')}")
                print(f"Score: {score.get('score')}")
                print(f"Category: {score.get('category')}")
                print(f"Description: {score.get('description')}")
                print(f"Last Updated: {score.get('lastUpdated')}\n")
        else:
            print(f"Error fetching secure scores. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    resource_id_to_query = "YOUR_CLOUD_RESOURCE_ID"
    get_secure_scores(resource_id_to_query)
