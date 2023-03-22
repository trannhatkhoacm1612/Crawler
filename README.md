# Crawler

Using module <span style = "color:green ">*request*</span> and <span style = "color:green ">*bs4*</span>to crawler a number of image from **google image** when input a search string.

## Idea

When we search somethings in the google image, the result is represented as a **HTML** file. Our duty is select the # <span style = "color:greeb">img tag</span> from this file, and download the # <span style = "color:green">"src"</span> atribute.



# Usage

1. Install the nearest vesion of important module

        pip install --upgrade requests

        pip install --upgrade beautifulsoup4

        pip install --upgrade chardet

2. *cd* to path that you want to place your image

        cd path/to/file

3. clone this repo

        git clone https://github.com/trannhatkhoacm1612/Crawler
3. Run the crawler.py

    You will call the <span style = "color:green">**download**</span> function and must input two parameters:

    - The **string** that to querry.

    - The **interer number** represented the number of img you want to download.
          
          download("dog",10) # install 10 img with the querry "dog" in google img

