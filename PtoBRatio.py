import time 
import urllib #for visting urls
from urllib.request import Request, urlopen

sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']

def yahooKeyStats(stock):
    try:
        #reading in all of the HTML sourcecode into memory
        sourcecode = urllib.urlopen('https://finance.yahoo.com/quote/',stock,'/key-statistics').read()
        #original link: https://finance.yahoo.com/quote/TSLA/key-statistics (replace TSLA with stock variable)
        
        #get Price to book Ratio, using a splitting to extract info needed
        pbr = sourcecode.split('Price/Book</span><!-- react-text: 59 --> <!-- /react-text --><!-- react-text: 60 -->(mrq)<!-- /react-text --><sup aria-label="KS_HELP_SUP_undefined" data-reactid="61"></sup></td><td class="Fz(s) Fw(500) Ta(end)" data-reactid="62">'[1].split('</td>')[0])
        print('price to book ratio for ' ,stock, 'is ' ,pbr)
        
        
    except Exception, e:
        print('Failed in the main loop' + str(e))

yahooKeyStats('aapl')


    

