# SoV-report-Automation
Automate the best seller SoV report for various brands from amazon shopping portal with web scraping.

ABSTRACT: 
To prepare a Share of Voice report of a brand under different categories from various online shopping portals. SoV (Share of Voice) is a measure of the market your brand owns compared to your competitors. It acts as a gauge for your brand visibility and how much you dominate the conversation in your industry. SoV is calculated as 
SoV= (Your brand metric/ Total market metric) * 100

TECHNICAL REQUIREMENTS: 
The code demands the requirement of the following:
1.	Google collab with requests, bs4, xlwt and re module.
2.	Microsoft Excel 2003 or higher versions.
3.	Internet connection.

INPUTS TO BE GIVEN: 
The code takes in 7 inputs from the user where all the brand names are to be given in lowercase letters:
1.	The brand whose SoV report is to be made.
2.	The number of competitors.
3.	The name of these competitors.
4.	The number of categories.
5.	The URL of these categories in the same order.
6.	The location where the file needs to be saved.
7.	The total number of items in a particular page.

OUTPUT: 
The SoV report will be stored in the given location as brandnameSoVreport.csv. The ouput will have the brand names along the columns and category names along the rows.

