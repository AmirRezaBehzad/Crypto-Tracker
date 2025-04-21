from celery import shared_task
from .models import DepositRequest

@shared_task
def confirm_deposit(deposit_id):
    deposit = DepositRequest.objects.get(id=deposit_id)
    
    # Simulate a blockchain "check"
    mock_blockchain = ["trx123456", "trx654321", "trx789123"]
    
    if deposit.trx_id in mock_blockchain:
        deposit.status = 'confirmed'
        deposit.save()

    return deposit.status


@shared_task
def test_celery_task():
    print("🚀 Celery task is working!")
