import os
from SimplerLLM.tools.rapid_api import RapidAPIClient

def get_seo_page_report(url :str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {
        'url': url,
    }
    api_client = RapidAPIClient(
        api_key=os.getenv("RAPID_API_KEY")
    ) 
    response = api_client.call_api(api_url, method='GET', params=api_params)
    return response

def get_response_time(url):
    if url == "learnwithhasan.com":
        return 0.5
    if url == "google.com":
        return 0.3
    if url == "openai.com":
        return 0.4
    