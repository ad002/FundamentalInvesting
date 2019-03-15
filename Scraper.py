import time 
import urllib #for visting urls
from urllib.request import Request, urlopen

sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']

def yahooKeyStats(stock):
    try:
        #reading in all of the HTML sourcecode into memory
        sourcecode=urllib.urlopen('https://finance.yahoo.com/quote/'+stock'/key-statistics').read()
        #original link: https://finance.yahoo.com/quote/TSLA/key-statistics (replace TSLA with stock variable)
        #get Price to book Ratio
        pbr = sourcecode.split('Price/Book</span><!-- react-text: 59 --> <!-- /react-text --><!-- react-text: 60 -->(mrq)<!-- /react-text --><sup aria-label="KS_HELP_SUP_undefined" data-reactid="61"></sup></td><td class="Fz(s) Fw(500) Ta(end)" data-reactid="62">'[1].split('</td>')[0]
        print('price to book ratio for ' ,stock, 'is ' ,pbr)
        
        
    except Exception,e:
        print('Failed in the main loop' + str(e))

yahooKeyStats('aapl')

#1. On homepage, find what you are looking for and copy/paste keyword 
#beloning to the value you want to scrape
#2. View page source, CMD+F plus keyword to find it in code
#3. Find what is on either side of the value on source code 
    #in this case: Price/Book</span><!-- react-text: 59 --> <!-- /react-text --><!-- react-text: 60 -->(mrq)<!-- /react-text --><sup aria-label="KS_HELP_SUP_undefined" data-reactid="61"></sup></td><td class="Fz(s) Fw(500) Ta(end)" data-reactid="62">
    #and </td> at the end and in between is our value (10.17 in that case)
#4. #Copy all from Price/Book to the value, split source code at that point
    #and mark it as element one so all BEFORE the Price/Book will be the
    #[0] element, Price/Book and all behind will be element [1], right 
    #now including our value 10,17 so we'll do another split by the closing
    #tag behind the value (</td>) and then the value 10,17 will be the 
    #[0] element or the first element
    
#5. What this does is split all the source code from all to the top 
    #until the value 10.17 and then split again what comes after it and 
    #put these elements in  a list 

    

