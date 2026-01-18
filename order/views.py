from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import stock,PlaceOrder
from django.core.mail import send_mail


# Create your views here.
@login_required
def makeorder(request):
    # TODOS: mail logic
    if request.method == "POST":
        user_id=request.user.id
        item_name = request.POST.get("item_name")
        quantity = request.POST.get("quantity")
        quantity1=stock.objects.get(item_name=item_name)
        quantity1.quantity=int(quantity1.quantity)-int(quantity)
        quantity1.save()
        c=PlaceOrder(
            user_id=user_id,
            item_name=item_name,
            quantity=quantity,
            price=quantity1.price,
        )
        c.save()
        print(f"Order received: {item_name}, Quantity: {quantity},{quantity1.quantity}")
        send_mail(
        subject='Test Email',
        message='This is a test email from Django',
        from_email='greninja100.game@gmail.com',
        recipient_list=[request.user.email],
        fail_silently=False,
    )

    products=stock.objects.all()
    return render(request, "order/order.html",{"products":products})


@login_required
def orderhistory(request):
    from .models import PlaceOrder
    orders = PlaceOrder.objects.filter(user_id=request.user.id).order_by('-order_date')
    return render(request, "order/vieworder.html", {"orders": orders})