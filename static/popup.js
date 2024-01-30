setTimeout(function () {
    var alert = document.getElementById('alert');
    alert.style.opacity = '0';
    setTimeout(function () {
        alert.style.display = 'none';
    }, 1000); 
}, 3000);