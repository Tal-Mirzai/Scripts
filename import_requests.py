import requests

def get_cat_fact():
    # Fetch a cat fact from the external website
    response = requests.get('https://catfact.ninja/fact')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        cat_fact = data['fact']
        return cat_fact
    else:
        return 'Failed to retrieve cat fact'

if __name__ == '__main__':
    cat_fact = get_cat_fact()
    print(f'Cat Fact: {cat_fact}')
