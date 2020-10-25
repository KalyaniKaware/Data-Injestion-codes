from bs4 import BeautifulSoup
from urllib import request
import requests
import pandas as pd

URL_to_scrape = "https://www.spotify.com/us/select-your-market/"


class APIcall:

    'API  -  https://restcountries.eu/rest/v2/alpha/{code}'
    def using_country_code(self, code):
        response = requests.get(f'https://restcountries.eu/rest/v2/alpha/{code}')
        data_dict = response.json()
        self.name = data_dict['name']
        self.region = data_dict['region']
        self.subregion = data_dict['subregion']
        self.latidude = data_dict['latlng'][0]
        self.longitude = data_dict['latlng'][1]
        self.population = data_dict['population']
        self.area = data_dict['area']
        self.gini = data_dict['gini']


class Scraper():
    def scrape(self, URL_to_scrape, parser):

        result_df = pd.DataFrame(
            columns=['name', 'region', 'subregion', 'latitude', 'longitude', 'population', 'area', 'gini',
                     'cost_string'])
        call = APIcall()
        count = 0

        response_page1 = request.urlopen(URL_to_scrape)
        soup1 = BeautifulSoup(response_page1, parser)

        '''<a class="market pull-left" href="/hk-zh/" lang="zh-HK" rel="hk-zh" title="香港（中文）">
                    <div class="media">
                    <div class="media-left media-middle">
                    <span class="media-object flag-icon"><img src="//country-flags.scdn.co/flags/hk.svg"/></span>
                    </div>
                    <div class="media-body media-middle text-black" dir="ltr">香港（中文）</div>
                    </div>
                    </a>
        '''
        for code in soup1.findAll('a', attrs={'class': "market pull-left"}):
            country_code = code['href'][1:3]
            response_page2 = request.urlopen(f'https://www.spotify.com/{country_code}/premium/?checkout=false')
            soup2 = BeautifulSoup(response_page2, 'html.parser')
            txt = soup2.find('h2', attrs={'class': "Type__TypeElement-sc-9snywk-0 iiNLPi sc-fznAgC leTPLB"})
            if txt == None:
                cost_string = soup2.find('h2').text
            else:
                cost_string = txt.text
            try:
                if country_code == 'uk':
                    country_code = 'gb'
                call.using_country_code(country_code)
            except:
                print(f'Couldnt get data for {country_code}')
            else:
                f = call.__dict__
                f['cost_string'] = cost_string
                result_df = result_df.append(f, ignore_index=True)
                count += 1
        print(f'Countries scraped for data: {count}')
        result_df.to_csv('result.csv')

bot = Scraper()
bot.scrape(URL_to_scrape, 'html.parser')
