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
filtered_Transaction = TransactionFilter.filter_by_state(Transaction) 
print("\nTransaction in Livorno:")
for Transaction in filtered_Transaction:
        print(f"- {Transaction.id} ({Transaction.ingress_hour}) - {Transaction.exit_hour}")
        if __name__ == "__main__":
            main()

