import requests


def iss_req():
    """Get current location of ISS"""
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    if r.status_code == 200:
        r_dict = r.json()
        current_position = r_dict['iss_position']
        print('Current position of ISS:', current_position)
        return current_position

    else:
        return "Error:", r.status_code
