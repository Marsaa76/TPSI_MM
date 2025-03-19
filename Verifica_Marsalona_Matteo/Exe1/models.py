class TransactionModel:

    def __init__(self, id, enter_site, ingress_hour, exit, exit_hour, amount):
        self.id = id
        self.enter_site = enter_site
        self.ingress_hour = ingress_hour
        self.exit = exit
        self.exit_hour = exit_hour
        self.amount = amount
@classmethod
def from_json(cls, data):

        return cls(
            id=data.get("id"),
            enter_site=data.get("enter_site"),
            ingress_hour=data.get("ingress_hour"),
            exit=data.get("exit"),
            email=data.get("email"),
            exit_hour=data.get("exit_hour"),
            amount=data.get("amount")
)
def __repr__(self):

    return f"TransactionModel(id={self.id}, enter_site='{self.enter_site}')"