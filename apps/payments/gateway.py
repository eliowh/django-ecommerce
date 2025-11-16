import uuid
from datetime import datetime

def process_payment(amount, currency='PHP', payment_method=None, **kwargs):
    """Mock payment processing for local products shopping site.
    
    Since this is a basic shopping site for local products with no real payment gateway required,
    this function simulates a successful payment process and returns a mock response.
    """
    # Generate a mock transaction ID
    transaction_id = str(uuid.uuid4())[:8].upper()
    
    # Mock payment response - always successful for demonstration
    return {
        'status': 'success',
        'transaction_id': transaction_id,
        'amount': str(amount),
        'currency': currency,
        'payment_method': payment_method or 'Cash on Delivery',
        'timestamp': datetime.now().isoformat(),
        'message': 'Order confirmed successfully!',
        'receipt_number': f'RCP-{transaction_id}'
    }