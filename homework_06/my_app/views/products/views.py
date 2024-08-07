from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)

from werkzeug.exceptions import (
    BadRequest,
)

from my_app.models import Product
from my_app.views.products.crud import products_storage as storage

products_app = Blueprint("products_app", __name__, url_prefix="/products")


@products_app.get("/", endpoint="list")
def get_products():
    products = storage.get()
    return render_template(
        "products/list.html",
        products=products,
    )


@products_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("product-name is required")
    product = storage.create(name=product_name)
    url = url_for("products_app.details", product_id=product.id)
    flash(f"Product {product.name} added successfully", category="success")
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    product: Product = storage.get_or_404(
        product_id=product_id,
    )

    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route(
    "/<int:product_id>/delete/",
    methods=["GET", "POST"],
    endpoint="delete",
)
def confirm_delete_product(product_id: int):
    product: Product = storage.get_or_404(
        product_id=product_id,
    )
    if request.method == "GET":
        return render_template(
            "products/delete.html",
            product=product,
        )

    product_name = product.name
    storage.delete(product)
    url = url_for("products_app.list")
    flash(f"Product {product_name} deleted", category="dark")
    return redirect(url)
