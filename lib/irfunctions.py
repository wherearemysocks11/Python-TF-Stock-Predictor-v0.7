urls = {
    'UK': 'https://',
    'US': 'https://',
    'EU': 'https://',
    'JA': 'https://',
    'CH': 'https://',
    'IN': 'https://'
}

def get_interest_rate():    
    try:
        pass
        
    except Exception as e:
        print(f"Error downloading interest rate data: {e}")
        return None