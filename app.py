
@app.route("/payment/qr/<int:order_id>")
def payment_qr(order_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    # Replace with your actual UPI ID
    upi_id = "YOUR_UPI_ID"

    # Adapt this query and field names to your Order model.
    order = Order.query.filter_by(id=order_id).first_or_404()

    # Ensure customers can only access their own orders.
    if order.user_id != session["user_id"]:
        abort(403)

    amount = float(order.total)
    if amount <= 0:
        abort(400)

    from urllib.parse import urlencode

    upi_url = "upi://pay?" + urlencode({
        "pa": upi_id,
        "pn": "Aqua Medicines",
        "am": f"{amount:.2f}",
        "cu": "INR",
        "tn": f"Order {order.id}"
    })

    qr = qrcode.make(upi_url)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template(
        "payment_qr.html",
        qr_base64=qr_base64,
        amount=amount,
        order=order
    )
:wq
