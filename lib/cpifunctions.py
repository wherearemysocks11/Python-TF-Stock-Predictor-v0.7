urls = {
    'UK': 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/d7g7/mm23',
    'US': 'https://',
    'EU': 'https://',
    'JA': 'https://',
    'CH': 'https://',
    'IN': 'https://'
}

def get_cpi_data(url):
    try:
        pass

    except Exception as e:
        print(f"Error downloading CPI data: {e}")
        return None
    