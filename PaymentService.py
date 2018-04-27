import stripe

class PaymentService(object):

    end_point='https://api.stripe.com'
    stripe.api_key='sk_test_edFqhGjHMIQrhYvbYm7KOk0U'

    def check_balance(self):
        return stripe.Balance.retrieve()

    def available_balance(self):
        balance = self.check_balance()
        return balance['available']

    def retrieve_balance_txn(self, txn_id):
        return stripe.BalanceTransaction.retrieve(txn_id)

    def balance_history(self):
        return stripe.BalanceTransaction.all()

    def create_charge(self, amount, currency, metadata, receipt_email, customer, source):
        return stripe.Charge.create(
            amount=amount,
            currency=currency,
            metadata=metadata,
            receipt_email=receipt_email,
            customer=customer,
            source=source
        )

    def retrieve_charge(self, charge_id):
        return stripe.Charge.retrieve(charge_id)

    def update_charge(self, charge_id, description):
        ch = stripe.Charge.retrieve(charge_id)
        ch.kk = description
        try:
            ch.save()
        except stripe.error.InvalidRequestError as e:
            print(e)

    def capture_charge(self, charge_id):
        ch = stripe.Charge.retrieve(charge_id)
        ch.capture()

    def list_charges(self, limit):
        return stripe.Charge.list(limit=limit)


ps = PaymentService()
ps.update_charge('ch_1B73duKkLxvTx1cOBdBxGySZ', 'we are fine')

