# NBA Stat Scraper

**NBA Stat Scraper** is a Python-based application that uses web scraping to fetch and display NBA player statistics. The program scrapes data from the official [NBA Stats](https://www.nba.com/stats) website and outputs relevant tables containing statistical information.

---

## Features

- **Scrapes NBA Stats**: Extracts player and team statistics from the official NBA stats website.
- **Dynamic Headers**: Parses table headers and corresponding data for an organized display.
- **Live Data**: Captures the latest data available on the NBA stats page.
- **Date Integration**: Displays the date alongside fetched statistics for context.

---

## Requirements

This project relies on the following Python libraries:

- `requests`: To make HTTP requests to the NBA stats website.
- `BeautifulSoup` (from `bs4`): To parse and scrape HTML content.

---

## Installation and Setup
1. Clone the repository or download the script:git clone https://github.com/your-repository/nba-stat-scraper.git

2. Navigate to the project directory:cd nba-stat-scraper

3. Ensure Python 3.8 or higher is installed on your system. You can download it from python.org.
   
4. Install the dependencies:
  ```bash
  pip install requests beautifulsoup4
  ```

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Execute the script:
   ```Python
   python main.py
   ```
4. View the parsed and printed statistics in the terminal.

---

## Code Breakdown
### URL and HTTP Request
The script fetches the HTML content of the NBA stats page:
```Python
URL = 'https://www.nba.com/stats'
response = requests.get(URL)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')
```

### Section and Table Parsing
Finds all sections containing tables and their respective headers:
```Python
sections = soup.find_all('section')
for section in sections:
    if section.find('table'):
        tables = section.find_all('table')
        title = section.find('h1')
        ...
```

### Data Extraction
Extracts rows and statistical data from each table:
```Python
for table in tables:
    rows = table.find_all('tr')
    header = table.find_previous('h2').text.strip()
    ...
    for row in rows:
        a_data = row.find_all('a')
        ...
```

### Output Formatting
The scraped data is formatted for terminal display, including section headers and results:
```Python
print(f'\n{"-"*40} \n --{title.text.strip()}-- (Today\'s Leaders {dt}) \n{"-"*40} \n')
print(header)
print('--------------------')
```

## Example Output
Sample output when the script is run:
```
---------------------------------------- 
 --Today's Leaders (2025-04-28)-- 
----------------------------------------

Points Leaders
--------------------
(LeBron James - Forward, 30.5)
(Stephen Curry - Guard, 29.7)

Assist Leaders
--------------------
(Luka Dončić - Guard, 10.3)
(Chris Paul - Guard, 9.8)
```

---

## Notes
- **Dynamic Data**: The script fetches live data from the NBA stats website. Ensure a stable internet connection when running the script.
- **HTML Structure**: The script relies on the current structure of the NBA stats page. If the page layout changes, adjustments to the parsing logic will be necessary.
- **Error Handling**: No robust error-handling mechanisms are included. Invalid HTTP responses or unexpected data formats may result in errors.



