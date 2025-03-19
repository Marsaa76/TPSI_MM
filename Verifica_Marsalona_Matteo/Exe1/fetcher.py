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
            Transaction_json = response.json()
            return [TransactionModel.from_json(Transaction) for Transaction in Transaction_json]
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []