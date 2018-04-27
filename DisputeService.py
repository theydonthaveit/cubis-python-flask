import stripe

class DisputeService(object):

    end_point='https://api.stripe.com'
    stripe.api_key='sk_test_edFqhGjHMIQrhYvbYm7KOk0U'

    def retrieve_dispute(self, dispute_id):
        return stripe.Dispute.retrieve(dispute_id)

    def update_dispute(self, dispute_id, evidence):
        dispute = self.retrieve_dispute(dispute_id)
        dispute.evidence = evidence
        dispute.save()