import requests
from bs4 import BeautifulSoup
import webbrowser

# Specify the URL of the news website
URL = "https://www.bbc.com/news"

# Make an HTTP GET request to the news website
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the news headlines
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")[:10]

    # Generate the HTML code for the news list
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>News Headlines</title>
    </head>
    <body>
      <h1>News Headlines</h1>

      <ul>
        {}
      </ul>
    </body>
    </html>
    """.format("\n    ".join(["<li>{}</li>".format(headline) for headline in headlines]))

    # Write the HTML code to a file
    with open("news.html", "w") as f:
        f.write(html_code)

    # Open the HTML file in a web browser
    webbrowser.open("news.html")

else:
    # Print an error message if the request was not successful
    print("Failed to retrieve data from news website.")
