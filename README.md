# <span style = "color:blue">Crawler</span>

Using module *request* and *bs4* to crawler a number of img from **google image** when input a search string.

## Idea

When we search somethings in the google image, the result is represented as a **HTML** file. Our duty is select the # <span style = "color:greeb">img tag</span> from this file, and download the # <span style = "color:blue">"src</span> atribute.



# Usage

1. Install the nearest vesion of *requests*, "bs4* and *chardet*

        pip install --upgrade requests

        pip install --upgrade beautifulsoup4

        pip install --upgrade chardet

2. *cd* to path that you want to place your image

3. clone this repo

3. Run the crawler.py
