import requests

class apicall:
    def using_country_code(self, code):
        '''API  -  https://restcountries.eu/rest/v2/alpha/{code}'''
        response = requests.get(f'https://restcountries.eu/rest/v2/alpha/{code}')
        data_dict = response.json()
        self.name = data_dict['name']
        self.region = data_dict['region']
        self.subregion =data_dict['subregion']
        self.latitude = data_dict['latlng'][0]
        self.longitude = data_dict['latlng'][1]
        self.population = data_dict['population']
        self.area = data_dict['area']
        self.gini = data_dict['gini']

c = apicall()
c.using_country_code('al')
print(type(c.__dict__))