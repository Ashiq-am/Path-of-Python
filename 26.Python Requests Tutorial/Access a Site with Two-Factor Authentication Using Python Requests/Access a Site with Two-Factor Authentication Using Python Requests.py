import requests

# Start a session
session = requests.Session()

# URL for the initial login (using reqres.in mock service)
login_url = "https://reqres.in/api/login"

# Payload for the initial login request
login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

# Initial login request
login_response = session.post(login_url, data=login_payload)
print("Initial login response:")
print(login_response)
print(login_response.json())  # Check the response text to see if 2FA is required

# Simulate a 2FA requirement check
two_fa_required = True

if two_fa_required:
    # Prompt for the 2FA code
    two_fa_code = input("Enter the 2FA code: ")

    # Mock URL for the 2FA verification (simulated endpoint)
    two_fa_url = "https://reqres.in/api/2fa"

    # Payload for the 2FA request
    two_fa_payload = {
        "2fa_code": two_fa_code
    }

    # Simulate the 2FA verification response
    two_fa_response = {
        "status": "success",
        "message": "Login successful"
    }

    # Check if 2FA verification was successful
    if two_fa_response["status"] == "success":
        print("Login successful!")
    else:
        print("2FA verification failed.")
else:
    print("Login failed or 2FA not required.")
