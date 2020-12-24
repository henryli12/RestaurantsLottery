import requests
import random
from restaurant import Restaurant


def search(term, loc):
    offset = random.randint(0, 100)
    API_KEY = '-COwCTyn3fqGSgl9aNSWg41eT-KUXYRkeIRZSyif7VL74L18RJ4eBewEOQUftIEpxLM1vbsSwfN1o6SM3RIA2irl8bnrm' \
              'OXLknSrXgqELBj5ld167oMGXSmWtKxYXXYx'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' %API_KEY}
    PARAMETERS = {'term': term,
                  'limit': 1,
                  'offset': offset,
                  'location': loc}
    response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)

    try:
        result = response.json()['businesses'][0]
    except IndexError:
        return Restaurant(name="NONE", url="NONE", stars="NONE", dollars="NONE", phone="NONE", address="NONE", categ="NONE")
    name = result['name']
    url = result['url'].split('?')[0]
    stars = str(result['rating'])
    try:
        dollars = result['price']
    except KeyError:
        dollars = 'Not Available'
    addresslist = result['location']['display_address']
    address = addresslist[0] + ", " + addresslist[1]
    categorieslist = result['categories']
    categ = []
    for i in categorieslist:
        categ.append(i['alias'])
    phone = result['display_phone']
    res = Restaurant(name=name, url=url, stars=stars, dollars=dollars, phone=phone, address=address, categ=categ)
    return res


if __name__ == '__main__':
    term = input("What are you looking for?  ")
    loc = input("Location:   ")
    print(search(term, loc))
