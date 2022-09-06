def totalPrice(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["car"].items():
            total= total + float(value["price"]) 
    else:
        total="you should login"

    return {"totalPrice": total}
