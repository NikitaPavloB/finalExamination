import requests
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_auth_token():
    response = requests.post(data['login_url'], data={"username": data['username'], "password": data['password']})

    if response.status_code == 200:
        user_id = response.json().get('id')
        return response.json()['token'], user_id
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        return None, None


def test_user_profile():
    token, user_id = get_auth_token()

    if token and user_id:
        headers = {
            "X-Auth-Token": token,
            "Content-Type": "application/json"
        }

        base_url = data['base_url']
        profile_url = f"{base_url}{user_id}"

        response = requests.get(profile_url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            print("Server response details:")
            print(f"    User ID: {user_data.get('id')}")
            print(f"    Username: {user_data.get('username')}")
            print(f"    First Name: {user_data.get('firstName')}")
            print(f"    Last Name: {user_data.get('lastName')}")
            print(f"    Phone: {user_data.get('phone')}")
            print(f"    Status: {user_data.get('status')}")
            print(f"    Sex: {user_data.get('sex')}")
            print(f"    Birth Date: {user_data.get('birthDate')}")
            print(f"    Avatar URL: {user_data.get('avatar', {}).get('cdnUrl')}")
            print()

            # Проверяем, что username в ответе совпадает с ожидаемым
            expected_username = data['username']
            actual_username = user_data.get('username')

            if actual_username == expected_username:
                print("User profile data matches the expected data.")
            else:
                print(f"Username mismatch. Expected: {expected_username}, Got: {actual_username}")

        else:
            print(f"Failed to get user profile. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    else:
        print("Failed to authenticate. No token or user_id obtained.")


# Запускаем функцию для тестирования
if __name__ == "__main__":
    test_user_profile()

