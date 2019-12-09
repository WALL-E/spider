#!/bin/bash

./3_downloader.py "http://dycg.dongying.gov.cn/sdgp2014/site/index.jsp" > 1.html
url=`./2_parse.py 1.html`
echo "市中标公告: "$url

./3_downloader.py $url > 3.html
urls=`./4_parse.py 3.html`
for i in $urls  
do   
    echo $i;  
done   
