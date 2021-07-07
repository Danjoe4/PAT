
function serve_button_links(link_data) {
    // button press for the product page
    document.getElementById("product_page").onclick = function () {
        location.href = link_data['product_page'];
    }

    // button press for the viewblock page
    document.getElementById("viewblock_page").onclick = function () {
        location.href = link_data['viewblock_page'];
    }
}

