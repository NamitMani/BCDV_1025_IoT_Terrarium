import requests

from config import BASE_URL


def get_server_status():
    try:

        response = requests.get(f'{BASE_URL}/status')

        if response and response.status_code == 200:
            return 'Online', None

    except Exception as e:
        return 'Offline', f'[Connection Error]: {e}'



if __name__ =='__main__':
    print(get_server_status())