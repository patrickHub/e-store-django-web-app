function zoomIn(event) {
  var element = document.getElementById("zoomPop");
  element.style.display = "inline-block";
  var img = document.getElementById("imgZoom");
  var posX = event.offsetX ? event.offsetX : event.pageX - img.offsetLeft;
  var posY = event.offsetY ? event.offsetY : event.pageY - img.offsetTop;
  element.style.backgroundPosition = -posX * 4 + "px " + -posY * 4 + "px";
}

function zoomOut() {
  var element = document.getElementById("zoomPop");
  element.style.display = "none";
}

function updateProductQuantityInCart() {
  $(".button-plus").on("click", function() {
    currentQuantityInput = $(this)
      .prev()
      .prev();
    currentQuantityInput.val(parseInt(currentQuantityInput.val()) + 1);
    console.log("quantity: ");
    document.getElementById("form-" + this.id).submit();
  });
  $(".button-minus").on("click", function() {
    currentQuantityInput = $(this).next();
    currentQuantityInput.val(parseInt(currentQuantityInput.val()) - 1);
    document.getElementById("form-" + this.id).submit();
  });
}
