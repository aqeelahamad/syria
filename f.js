
function my(){
var request = require('request');
var cheerio = require('cheerio');
var text='';
request({
  uri: "http://finance.yahoo.com/q?s=AAPL",
}, function(error, response, body) {
	var $ = cheerio.load(body);
  
 $('.rtq_table').each(function(){
  	var data = $(this);
  	//var text = console.log(data.html())
  	var text=console.log(data.text().replace(/["']/g,'\\"'));
  

                                  });
				 });
	return text;
          }

function n(){
  return 5
}
//a=console.log(my())
function c(){
//var b=my();
return my(); }
my()
//console.log('"'+a+'"')
//c()
 //console.log(y.replace(/"/g,"'"))





