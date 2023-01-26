import requests
import urllib
import json
class IPQS:
    key = 'JAEvaHs7q9yYVhuWRL3tm7sLc1iqRRNq'
    def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
        url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
        x = requests.get(url, params = vars)
        #print(x.text)
        return (json.loads(x.text))
if __name__ == "__main__":
    url = input("Enter the URL >> ")
    strictness = 0
    additional_params = {
        'strictness' : strictness
    }
    ipqs = IPQS()
    result = ipqs.malicious_url_scanner_api(url, additional_params)
    if 'success' in result and result['success'] == True:
        print(result['domain'])
