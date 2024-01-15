document.querySelectorAll('.quantity').forEach(function (quantity) {
    quantity.addEventListener('change', function () {
        var price = parseFloat(this.dataset.price);
        var total = this.value * price;
        this.parentElement.nextElementSibling.nextElementSibling.textContent = total.toFixed(2);
        updateTotal();

        // Send AJAX request
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update_quantity/');
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('Quantity updated');
            }
        };
        xhr.send('product_id=' + this.dataset.productId + '&quantity=' + this.value);
    });
});