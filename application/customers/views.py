from application import app, db
from flask import redirect, render_template, request, url_for
from application.customers.models import Customer


@app.route("/customers", methods=["GET"])
def customers_index():
    return render_template("customers/list.html", customers=Customer.query.all())


@app.route("/customers/new/")
def customers_form():
    return render_template("customers/new.html")


@app.route("/customers/", methods=["POST"])
def customers_create():
    c = Customer(request.form.get("customer_name"), request.form.get("customer_address"))

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("customers_index"))


@app.route('/delete/<int:id>')
def delete(id):
    customer_to_delete = Customer.query.get_or_404(id)

    db.session.delete(customer_to_delete)
    db.session.commit()

    return redirect(url_for("customers_index"))


@app.route('/update/<int:id>', methods=["GET","POST"])
def update(id):
    customer = Customer.query.get_or_404(id)

    if request.method == 'POST':

        customer.name = request.form['customer_name']
        customer.address = request.form['customer_address']

        db.session.commit()
        return redirect('/customers')
    
    else:
        return render_template('customers/update.html', customer=customer)