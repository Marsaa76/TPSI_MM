from urllib import response
import requests
from config import API_URL
from models import TransactionModel
from datetime import datetime
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

root = ET.fromstring(response.text)
Transactions = []
for Transaction in root.findall("transazione"):
     Transactions.append(Transaction(
        id = int (Transaction.find("id").text),
        enter_site=Transaction.find("enter_site").text,
        ingress_hour = datetime.fromisoformat(Transaction.find("ingress_hour").text),
        exit = Transaction.find("exit").text,
        exit_hour = datetime.fromisoformat(Transaction.find("exit_hour").text),
        amount = float(Transaction.find)("amount").text
        ))