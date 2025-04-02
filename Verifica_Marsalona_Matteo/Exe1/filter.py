from config import DEFAULT_STATE_FILTER
from datetime import datetime
class TransactionFilter:
    @staticmethod
    def filter_by_state(Transactions, enter_site=DEFAULT_STATE_FILTER):
        return [Transaction for Transaction in Transactions if Transaction.enter_site == enter_site]
    
    def count_enter_site_Livorno(Transactions):
        return sum (1 for t in Transactions if t.enter_site == "Livorno")
    
    def count_total_amount(Transactions):
        return sum (t.amount for t in Transactions)
    
    def count_total_time(Transactions):
        return sum (int((t.exit_hour - t.ingress_hour).total_seconds()) for t in Transactions)