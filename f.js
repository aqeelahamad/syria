
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
  	var text=console.log('"'+data.html().replace(/["]/g,'\\"')+'"');
  

                                  });
				 });
	return text;
          }

function n(){
  return 5
}
//a=console.log(my())
function scrap(){
 b="http://finance.yahoo.com/q?s=AAPL";
$.ajax({
     url: b,
     dataType: 'text',
     success: function(data) {
              $('.rtq_table').each(function(){
  	var data = $(this);
  	var text='"'+data.html().replace(/["]/g,'\\"')+'"';
  	//var text=data.html();
  

                                  });
               
                             
                               }
        });

            

	return text;
                    }

function c(){
//var b=my();
return my(); }
scrap()
//console.log('"'+a+'"')
//c()
 //console.log(y.replace(/"/g,"'"))





