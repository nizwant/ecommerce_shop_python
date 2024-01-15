setTimeout(function () {
    var alert = document.getElementById('alert');
    alert.style.opacity = '0';
    setTimeout(function () {
        alert.style.display = 'none';
    }, 1000); /* Wait for the transition to complete */
}, 3000); /* Start the fade out after 1 second */