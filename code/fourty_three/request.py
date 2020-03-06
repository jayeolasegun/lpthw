from urllib.request import urlopen

url = urlopen("https://www.cbn.gov.ng/Currency/securityfeatures/SecurityFeatures")

#name = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(url.read())