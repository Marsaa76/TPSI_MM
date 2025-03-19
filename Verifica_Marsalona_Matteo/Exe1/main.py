import datetime
from urllib import response
from fetcher import TransactionFetcher
from filter import TransactionFilter
def main():
    fetcher = TransactionFetcher()
    transactions = fetcher.fetch_Transactions()
    if not transactions:
        print("No transactions found or API request failed.")
        return
    filtered_Transaction = TransactionFilter.filter_by_state(transactions) 
    print("\nTransaction in Livorno:")
    for transaction in filtered_Transaction:
            print(f"- {transaction.id} ({transaction.ingress_hour}) - {transaction.exit_hour}")
            if __name__ == "__main__":
                main()

