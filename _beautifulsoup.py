html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>first web page</title>
</head>
<body>
    <h1>
        Python Kursu
    </h1>

        <div class="grup1">
            <h2>
                Programlama
            </h2>
        </div>
<u>

        
    <li>
         menü3
    </li>
</u>

</body>
</html>

"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') 

result = soup.prettify()

print(result)
result = soup.title
result = soup.body
result = soup.head

result = soup.title.name

result = soup.h1
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string


result = soup.find_all('h2')

result = soup.div
result = soup.find_all('div')

result = soup.div.fincChild()

