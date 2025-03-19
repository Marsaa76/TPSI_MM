import datetime
from urllib import response
from fetcher import TransactionFetcher
from filter import TransactionFilter
def main():
    fetcher = TransactionFetcher()
    Transactions = fetcher.fetch_TRansactions()
    if not Transactions:
        print("No transactions found or API request failed.")
        return
filtered_Transaction = TransactionFilter.filter_by_state(Transactions) 
print("\nTransaction in Livorno:")
for Transaction in filtered_Transaction:
        print(f"- {Transaction.id} ({Transaction.ingress_hour}) - {Transaction.exit_hour}")
        if __name__ == "__main__":
            main()

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