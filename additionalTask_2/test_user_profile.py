import requests
import yaml
import pytest

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture
def token_and_id():
    response = requests.post(data['login_url'], data={"username": data['username'], "password": data['password']})

    if response.status_code == 200:
        user_id = response.json().get('id')
        return response.json()['token'], user_id
    else:
        pytest.fail(f"Failed to authenticate. Status code: {response.status_code}")
        return None, None


def test_user_profile(token_and_id):
    token, user_id = token_and_id

    # Проверка наличия токена и user_id
    assert token is not None, "Token is not obtained"
    assert user_id is not None, "User ID is not obtained"

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }

    base_url = data['base_url']
    profile_url = f"{base_url}{user_id}"

    response = requests.get(profile_url, headers=headers)

    assert response.status_code == 200, f"Failed to get user profile. Status code: {response.status_code}"

    user_data = response.json()

    # Словарь для хранения данных для вывода
    output_data = {
        "User ID": user_data.get('id'),
        "Username": user_data.get('username'),
        "First Name": user_data.get('firstName'),
        "Last Name": user_data.get('lastName'),
        "Phone": user_data.get('phone'),
        "Status": user_data.get('status'),
        "Sex": user_data.get('sex'),
        "Birth Date": user_data.get('birthDate'),
        "Avatar URL": user_data.get('avatar', {}).get('cdnUrl')
    }

    # Вывод детализированной информации о пользователе
    print("User profile details:")
    for key, value in output_data.items():
        print(f"    {key}: {value}")

    # Проверяем, что username в ответе совпадает с ожидаемым
    expected_username = data['username']
    actual_username = user_data.get('username')

    assert actual_username == expected_username, f"Username mismatch. Expected: {expected_username}, Got: {actual_username}"
