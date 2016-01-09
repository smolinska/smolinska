$(document).ready(function () {
    var url = window.location.href;
    console.log(url);
    if (url.indexOf('#') < 0) {
        window.location.replace(url + "#");
    } else {
        window.location.replace(url);
    }
});