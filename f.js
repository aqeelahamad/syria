function my(){
var request = require('request');
var cheerio = require('.node_modules/cheerio');
var text='';
request({
  uri: "http://finance.yahoo.com/q?s=AAPL",
}, function(error, response, body) {
	var $ = cheerio.load(body);
  
 $('.rtq_table').each(function(){
  	var data = $(this);
  	//var text = console.log(data.html())
  	var text=console.log('"'+data.html().replace(/["]/g,'\\"')+'"');
  

                                  });
				 });

}

my()

