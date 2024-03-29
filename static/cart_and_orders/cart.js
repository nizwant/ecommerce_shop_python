function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to update the total price of the order
function updateGrandTotal() {
    var grandTotal = 0;
    document.querySelectorAll('.total').forEach(function (total) {
        grandTotal += parseFloat(total.textContent);
    });
    document.getElementById('grandTotal').textContent = grandTotal.toFixed(2);
}

// Function to update the price of an items = quantity * price
function updateTotalPrice(quantityInput) {
    var price = parseFloat(quantityInput.dataset.price);
    var quantity = parseInt(quantityInput.value);
    var total = price * quantity;
    var totalElement = quantityInput.parentElement.nextElementSibling.nextElementSibling;
    totalElement.textContent = total.toFixed(2) + " zł";
}

function showToast(message) {
    var toast = document.getElementById("toast");
    toast.className = "show";
    toast.innerText = message;
    setTimeout(function(){ toast.className = toast.className.replace("show", ""); }, 3000);
}

document.addEventListener('DOMContentLoaded', function () {
    // Calculate and update the total and the grand total when the page is loaded
    document.querySelectorAll('.quantity').forEach(function (quantity) {
        updateTotalPrice(quantity);
    });
    updateGrandTotal();

    document.querySelectorAll('.remove').forEach(function (button) {
        button.addEventListener('click', function () {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/orders/remove_item/');
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function () {
                if (xhr.status === 200) {
                    showToast('Item removed successfully');
                    location.reload();
                }
            };
            xhr.send('product_id=' + this.dataset.productId);
        });
    });

    document.getElementById('finalizeOrder').addEventListener('click', function () {
        location.href = '/orders/finalize_order/';
    });

    // Event listener for quantity inputs
    document.querySelectorAll('.quantity').forEach(function (quantity) {
        quantity.addEventListener('change', function () {
            if (this.value == 0) {
                // Remove item if quantity is 0
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/orders/remove_item/');
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        showToast('Item removed successfully');
                        location.reload();
                    }
                };
                xhr.send('product_id=' + this.dataset.productId);
            } else {
                // Update quantity
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/orders/update_quantity/');
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        showToast('Quantity updated successfully');
                    }
                };
                xhr.send('product_id=' + this.dataset.productId + '&quantity=' + this.value);

                // Update totals immediately after quantity is changed
                updateTotalPrice(this);
                updateGrandTotal();
            }
        });
    });
});
