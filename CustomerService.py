import stripe

class CustomerService(object):

    end_point='https://api.stripe.com'
    stripe.api_key='sk_test_edFqhGjHMIQrhYvbYm7KOk0U'

    def create_customer(self, email, metadata, exp_month, exp_year, number, cvc, object='card'):
        stripe.Customer.create(
            email=email,
            metadata=metadata,
            source={
                'object':object,
                'exp_month':exp_month,
                'exp_year':exp_year,
                'number':number,
                'cvc':cvc
            }
        )

    def retrieve_customer(self, customer_id):
        return stripe.Customer.retrieve(customer_id)

    def update_customer(self, customer_id, description):
        cu = self.retrieve_customer(customer_id)
        cu.description = description
        cu.save()

    def detelet_custimer(self, customer_id):
        cu = self.retrieve_customer(customer_id)
        cu.delete()

    def list_customers(self, limit):
        return stripe.Customer.list(limit=limit)