urls = {
    'UK': 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/grossdomesticproductgdp/timeseries/ybha/pn2',
    'US': 'https://',
    'EU': 'https://',
    'JA': 'https://',
    'CH': 'https://',
    'IN': 'https://'
}

def get_gdp_data(url):
    try:
        pass
    
    except Exception as e:
        print(f"Error downloading GDP data: {e}")
        return None