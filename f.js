
function my(){
var request = require('request');
var cheerio = require('cheerio');

request({
  uri: "http://finance.yahoo.com/q?s=AAPL",
}, function(error, response, body) {
	var $ = cheerio.load(body);
  
 $('.rtq_table').each(function(){
  	var data = $(this);
  	var text = data.html();
  	return text

                                  });
     return text   });

   return text        }

var x=my()

console.log(x)


 





