function updateTotal() {
    var grandTotal = 0;
    document.querySelectorAll('.total').forEach(function (total) {
        grandTotal += parseFloat(total.textContent);
    });
    document.getElementById('grandTotal').textContent = grandTotal.toFixed(2);
}

document.querySelectorAll('.quantity').forEach(function (quantity) {
    quantity.addEventListener('change', function () {
        var price = parseFloat(this.dataset.price);
        var total = this.value * price;
        this.parentElement.nextElementSibling.nextElementSibling.textContent = total.toFixed(2);
        updateTotal();

        // Send AJAX request to update quantity
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update_quantity/');
        xhr.setRequestHeader('X-CSRFToken', document.getElementById('csrfToken').value);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('Quantity updated');
            }
        };
        xhr.send('product_id=' + this.dataset.productId + '&quantity=' + this.value);
    });
});

document.querySelectorAll('.remove').forEach(function (remove) {
    remove.addEventListener('click', function () {
        var row = this.parentElement.parentElement;
        row.parentElement.removeChild(row);
        updateTotal();

        // Send AJAX request to remove item
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/remove_item/');
        xhr.setRequestHeader('X-CSRFToken', document.getElementById('csrfToken').value);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('Item removed');
            }
        };
        xhr.send('product_id=' + this.dataset.productId);
    });
});

updateTotal();