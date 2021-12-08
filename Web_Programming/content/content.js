document.getElementById("form").onsubmit = function () {
  var font_size = document.getElementById("input");
  var now = document.getElementById("now");
  console.log(font_size.value);
  changefontsize(font_size);
  now.innerHTML = "현재: " + font_size.value + "px";
  return false;
};
text = document.getElementById("text");
function changefontsize(font_size) {
  text.style.fontSize = font_size.value + "px";
}
var input = document.getElementById("input");
var output = document.getElementById("output");
input.oninput = function () {
  output.innerHTML = "희망: " + this.value + "px";
};
