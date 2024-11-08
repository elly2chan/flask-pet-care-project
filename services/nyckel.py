import requests
from decouple import config


class NyckelService:
    def __init__(self):
        self.token_url = config('NYCKEL_TOKEN_URL')
        self.api_url = config('NYCKEL_API_URL')
        self.client_id = config('NYCKEL_CLIENT_ID')
        self.client_secret = config('NYCKEL_CLIENT_SECRET')
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Obtain the access token using client credentials."""
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.token_url, data=data)
        response_data = response.json()
        access_token = response_data.get('access_token')

        if not access_token:
            raise ValueError("Access token not found in response")
        return access_token

    def identify_dog_breed(self, data):
        """Invoke the dog breed identifier function."""
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        payload = {
            "data": data
        }
        response = requests.post(self.api_url, headers=headers, json=payload)
        return response.json()
