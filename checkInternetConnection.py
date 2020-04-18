import time
import state

#make cross compatible between Python 2 and 3
try:
    # original
    import urllib2
# for Python 3
except ImportError:
    import urllib.request as urllib2

# Check connectivity to the internet and save the results as state.InternetIsUp
def isitup():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1).close()
    except urllib2.URLError:
        print ("Internet Not Connected")
        time.sleep(1)
        state.InternetIsUp = False
    else:
        print ("Internet Connected")
        state.InternetIsUp = True