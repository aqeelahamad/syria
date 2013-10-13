
function my(){
var request = require('request');
var cheerio = require('cheerio');
var text=''
request({
  uri: "http://finance.yahoo.com/q?s=AAPL",
}, function(error, response, body) {
	var $ = cheerio.load(body);
  
 $('.rtq_table').each(function(){
  	var data = $(this);
  	var text = console.log(data.html());
  

                                  });
				 });
	return text
          }

function n(){
  return 5
}

function c(){
var b=n()
return b+2; }

my()

 





