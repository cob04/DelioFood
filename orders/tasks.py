from django.core.mail import send_mail

from .models import Order


def send_order_email(order_id):
    """
    Send email order notification.
    """
    order = Order.objects.get(id=order_id)
    subject = str(order)
    message = "Dear {}, \n\nYour have successfully placed an order.\
        \nYour order is being processed and a delivery will follow.\
        \n Thank You,\n KitchenPass Team.".format(order.billing_name())
    mail_sent = send_mail(subject,
                        message,
                        'noreply@kitchenpass.co.ke',
                        [order,email])
    return mail_sent
