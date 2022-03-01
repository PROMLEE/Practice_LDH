var Links = {
  SetColor: function (color) {
    // var alist = document.querySelectorAll("a");
    // var i = 0;
    // while (i < alist.length) {
    //   alist[i].style.color = color;
    //   i += 1;
    // }
    $('a').css('color', color);
  }
}

var Body = {
  SetColor: function (color) {
    // document.querySelector("body").style.color = color;
    $('body').css('color', color);
  },
  SetBackgroundColor: function (color) {
    // document.querySelector("body").style.backgroundColor = color;
    $('body').css('backgroundColor', color);
  },
}

function nightDayHandler(self) {
  if (self.value === "night") {
    Links.SetColor("powderblue");
    Body.SetBackgroundColor("black");
    Body.SetColor("white");
    self.value = "day";
  } else {
    Links.SetColor("blue");
    Body.SetBackgroundColor("white");
    Body.SetColor("black");
    self.value = "night";
  }
}