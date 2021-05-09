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
        return "Error: ", r.status_code


def astro_names():
    """Get current names of astronauts on ISS """
    url = 'http://api.open-notify.org/astros.json'
    r = requests.get(url)
    if r.status_code == 200:
        r_dict = r.json()
        # Get names on ISS:
        people = [x['name'] for x in r_dict['people'] if x['craft'] == 'ISS']
        return people
    else:
        return "Error: ", r.status_code