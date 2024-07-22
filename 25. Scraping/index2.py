
from facebook_scraper import get_profile
import locale
locale.setlocale(locale.LC_ALL, 'en_US') 

# get_profile("zuck") # Or get_profile("zuck", cookies="cookies.txt")
get_profile("maseeh.niazai", cookies="cookies.txt")