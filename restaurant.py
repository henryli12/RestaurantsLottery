class Restaurant:
    def __init__(self, name, url, stars, dollars, phone, address, categ):
        self.name = name
        self.url = url
        self.stars = stars
        self.dollars = dollars
        self.phone = phone
        self.address = address
        self.categ = categ

    def __str__(self):
        return "name: " + str(self.name) + "\nurl: " + str(self.url) + "\nstars: " + str(self.stars)\
               + "\ndollars: " + str(self.dollars) + "\nphone: " + str(self.phone) + "\naddress: " + str(self.address)\
               + "\ncategories: " + str(self.categ)
