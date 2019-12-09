#!/bin/bash

./downloader.py "http://dycg.dongying.gov.cn/sdgp2014/site/index.jsp" > 1.html
url=`./1_parse.py 1.html`
echo "市中标公告: "$url

./downloader.py $url > 2.html
urls=`./2_parse.py 2.html`
for i in $urls  
do   
    echo $i;  
    ./downloader.py $i > 3.html
    ./3_parse.py 3.html
done   
