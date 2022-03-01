// var request = require('request'), cheerio = require('cheerio');
// var url = "http://codenamu.org/blog/";

// request(url, function (err, res, html) {
//   if (!err) {
//     var $ = cherrio.load(html)
//     $(".entry-title > a").each(function () {
//       var post = { "title": "", "link": "", "summary": "", "category": [] };
//       var data = $(this);
//       post["title"] = data.text();
//       post["link"] = data.attr("href");
//     })
//     $(".entry-summary > p").each(function (i) { })
//     $(".entry-categories > p").each(function (i) {
//       $(this).children().each(function () { })
//     })
//   }

// })
// const request = new XMLHttpRequest();
// const url = "https://www.naver.com";
// fetch(url, options)
//   .then((response) => console.log("response:", response))
//   .catch((error) => console.log("error:", error))
fetch("https://jsonplaceholder.typicode.com/posts/1").then((response) => console.log(response));