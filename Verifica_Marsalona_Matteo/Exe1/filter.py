from config import DEFAULT_STATE_FILTER
class TransactionFilter:
    @staticmethod
    def filter_by_state(Transaction, enter_site=DEFAULT_STATE_FILTER):
        return [Transaction for TRansaction in Transaction if Transaction.enter_site == enter_site]