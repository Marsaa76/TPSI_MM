import requests
from config import API_URL
from models import TransactionModel
class TransactionFetcher:
    def __init__(self, url=API_URL):
        self.url = url
    def fetch_Transaction(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            Transaction_xml = response.xml()
            return [TransactionModel.from_xml(Transaction) for Transaction in Transaction_xml]
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []