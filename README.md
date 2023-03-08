# SecondTask_CAS

  #### Udemy Course Cupon Scraper Task 
### Before moving on to the usage and explanation of the code, the code contains a GUI.py file, but this GUI is a very non-functional and even visually inadequate UI written in PyQt5. The main purpose of this code is to be adapted to the website. At the end of the task delivery process, by adapting this application to my Django project, it will be possible to access it over the hasankayan.net domain, which I will publish over Amazon EC2. Django work is not complete yet so I wrote a simple website, which hosts a .csv file generated with my scraper code in the background and downloads it when the button is pressed. I am hosting this demo website via Github Pages. Please visit this page for my interface design and simple logic.

### Coding All Stars Second Task 


![web-scraping-with-python](https://user-images.githubusercontent.com/80827760/223840296-d74ccc09-77ce-46f5-b89f-d5c499e0e5a3.png)



# Udemy Coupon Scraper

This is a Python script that scrapes Udemy coupons from three different websites: real.discount, discudemy.com, and couponscorpion.com. It uses Selenium and BeautifulSoup libraries to navigate the webpages, extract data and write to a CSV file.

Before we start lets make a preparation. 

### NOTE : The code was previously prepared on the Linux operating system, but it was organized according to Windows. If you are going to run it on a Linux or Mac device, you need to make path arrangements.

## Prerequests 

- Python 3.11.2 or later version should be installed on your system.
- Chrome driver only supports for 111 version, so be check your Chrome browser version. 
- Before you run the code you need to install all libraries, to do that I created a 'requirements.txt' file you cann call it at the terminal to install all needed libraries. How call 'requirements.txt' :
    . Open your terminal
    .Run this command : pip install -r requirements.txt

Now lets make these steps together...

- Open Visal Studio Code --> File --> Open Folder --> SecondTask_CAS 
- Open a new terminal 
- Run " pip install -r requirements.txt " command at terminal:

![image](https://user-images.githubusercontent.com/80827760/223865374-9f7d883b-e2b8-4a76-8d0e-a7a481b230a3.png)
For me, it says "Requirement already satisfied:" but in your computer packages will be downloading.ç 
- Now lets run the script by the command: " python scrapy.py " 
- It will ask for page number that you want enter those values as you wish. 

![image](https://user-images.githubusercontent.com/80827760/223869442-b1fa25d9-c910-42a1-bac1-a176962b9abc.png)


It will start running image above and tell you what it is doing step by step. 
#### In this process, some pages may be opened and closed, you should not interfere with these pages manually.

![image](https://user-images.githubusercontent.com/80827760/223866017-082dafc4-adc8-4b61-a567-73945e02b944.png)

This takes a while, do not close the program, it says if there is an error. 
- While checking whether the courses are still discounted on Udemy, you will see pages like the one below, don't worry, these pages are opened independently of your personal Udemy accounts.

![image](https://user-images.githubusercontent.com/80827760/223867907-d168ad46-0b11-47ed-99b2-1581b4529b3c.png)

- If a sufficient number of courses cannot be obtained, the expression seen in the photo below appears and starts to scan the second site, if there is not enough number here, it will start to scan the 3rd site. The more sites you enter, the longer the process will take.


  print("There are not enougf cupons, to complete cupon number into "+str(exportLineSize)+", starting to scrap", discUdemyURL)
  
  If second scrap is also not enough you will see the output of 
  
  print("There are not enougf cupons, to complete cupon number into "+str(exportLineSize)+", starting to scrap", cuponScorpionURL) 
 
 
- When scraping process completed you can open the output.csv file to see your cupons. 

![image](https://user-images.githubusercontent.com/80827760/223869898-2794d6fe-1326-4315-b7ba-05a092a0e210.png)

  
## How Does Code Works Step-by-Step

 ## Udemy(func)  Function 
 
- The first line driver.maximize_window() maximizes the browser window of the Selenium driver.
- The function then loops through each URL in the finurls list (which is not defined in this function and is presumably defined elsewhere in the code).
- After loading each URL with driver.get(data), the function waits for 3 seconds to let the page load.
- The function then uses BeautifulSoup to parse the HTML content of the page.
- The code tries to find a "Free tutorial" badge on the page. If it finds one, it skips to the next URL.
- If no "Free tutorial" badge is found, the code extracts the course link, coupon code, course name, and course expiration date (if available) from the page using various BeautifulSoup methods.
- If the number of courses scraped so far is greater than or equal to exportLineSize (which is not defined in this function and is presumably defined elsewhere in the code), the function calls printer() to export the scraped data to a CSV file and exits the loop.
- If there are not enough coupons to meet the exportLineSize requirement, the function calls either the realDiscount() or cuponScorpion() function (which are not defined in this function and are presumably defined elsewhere in the code) to scrape more coupon links from other websites.
- If there are no more URLs to scrape, the function calls printer() to export the scraped data to a CSV file

## realDiscount(url)  Function

- The function loads the given URL using driver.get(url) and waits for up to 30 seconds for a button with class "btn-primary" to appear on the page using WebDriverWait and EC.presence_of_element_located. If the button does not appear within 30 seconds, the function prints an error message and quits the browser.
- The function uses BeautifulSoup to parse the HTML content of the page.
- the code extracts the list of coupon links from the page by finding the container div element with class "mt-4" and then all the li elements within it using various BeautifulSoup methods.
- If the number of links scraped is less than linkPerSite (which is not defined in this function and is presumably defined elsewhere in the code), the function clicks the "btn-primary" button repeatedly until it loads enough links.
- For each link, the function checks if the time to expiration is less than 2 days (i.e., 49 hours) using BeautifulSoup methods. If it is, the function adds the link to the links list.
- The function then minimizes the browser window and prints a message to indicate that web scraping is a long process.
- For each link in the links list, the function sends a request to the link with requests.get() and checks if the response status code is 200. If it is, the function uses BeautifulSoup to extract the Udemy course link with a coupon code from the page.
- If the extracted link contains "https://www.udemy.com/course" and "couponCode=" (i.e., it is a valid Udemy course link with a coupon code), the function adds the link to the finurls list.
- The function then calls the udemy("realDiscount") function to scrape more Udemy coupon links if necessary. 

## discUdemy(url)  Function

- The function sends a request to the given URL using requests.get() and checks if the response status code is 200. If it is, the function uses BeautifulSoup to parse the HTML content of the page and extracts the maximum page number of the pagination section.
- The function then loops through each page in the pagination section and sends a request to the page URL with requests.get() and checks if the response status code is 200. If it is, the function extracts the list of coupon links from the page by finding the container article element with class "four" and then all the section elements with class "card" within it using various BeautifulSoup methods. The function then checks if the coupon was added "Today" or "Yesterday" using the tempdate variable and adds the link to the links list if it was.
- If the number of links scraped is greater than linkPerSite (which is not defined in this function and is presumably defined elsewhere in the code), the function breaks out of the loop.
- The function then loops through each link in the links list and sends a request to the link with requests.get(). If the response status code is 200, the function uses BeautifulSoup to extract the Udemy course link with a coupon code from the page.
- If the extracted link contains "couponCode=" (i.e., it is a valid Udemy course link with a coupon code), the function adds the link to the finurls list.
- The function then calls the udemy("discUdemy") function to scrape more Udemy coupon links if necessary.

## cuponScorpion(url) Function

- The function sends a request to the given URL using driver.get() and waits for 2 seconds. The function then uses BeautifulSoup to parse the HTML content of the page and extracts the maximum page number of the pagination section.
- The function then loops through each page in the pagination section by sending requests to the page URL with driver.get() and waits for 2 seconds. The function extracts the list of coupon links from the page by finding the container div element with class "pt5" and then all the article elements with class "col_item" within it using various BeautifulSoup methods. The function then checks if the coupon was added "Today", "1 day", or less than 1 day ago using the datetest variable and adds the link to the links list if it was.
- If the number of links scraped is greater than linkPerSite (which is not defined in this function and is presumably defined elsewhere in the code), the function breaks out of the loop.
- The function then loops through each link in the links list and sends a request to the link with driver.get() and waits for 2 seconds. If the link contains "javascript:void(0)", the function waits for 1 second and tries again until it finds a valid link. The function then uses BeautifulSoup to extract the Udemy course link with a coupon code from the page.
- If the extracted link contains "couponCode=" (i.e., it is a valid Udemy course link with a coupon code), the function adds the link to the finurls list.
- The function then calls the udemy("cuponScorpion") function to scrape more Udemy coupon links if necessary.


## printer() Function 

- The function prints a message indicating that scraping is completed and that it is starting to write the output file.
- The function opens the "output.csv" file in write mode using open() and creates a csv.writer object called writer.
- The function writes the fieldnames to the first row of the CSV file using writer.writerow(). The fieldnames are "Course Name", "Course Link", "Coupon", and "Expiration".
- The function loops through the scraped course information using a for loop with the range() function and len() function to iterate over the length of the coursename list (assuming all lists have the same length). In each iteration, the function writes the course name, course link, coupon code, and expiration date to a row in the CSV file using writer.writerow().
- The function prints a message indicating that scraping is completed and closes the CSV file using result.close().
- The function quits the driver session using driver.quit().


### realDiscount(realDiscountURL)

At the end of the code, we only need to call the realDiscount() function. If this function does not provide enough coupons, it calls the other function, and other functions work in the same way.

## Summary 

In summary,  code is a Python script that scrapes Udemy coupon codes from various websites and writes the information to a CSV file called "output.csv". The script uses the Selenium and BeautifulSoup libraries to scrape the web pages and extract the relevant information.
The code begins by importing the necessary libraries and setting some constants and variables, including the driver object for Selenium and lists for storing the scraped course information.
The script then defines three functions: realDiscount(), discUdemy(), and cuponScorpion(). These functions each scrape coupon codes from a different website using Selenium and/or BeautifulSoup and add the scraped information to the corresponding global lists.
After defining the functions, the script calls the realDiscount() function with a URL for the "real.discount" website to start the scraping process. If there are not enough coupon codes scraped from this website, the function will call the discUdemy() function with a URL for the "discudemy" website and then the cuponScorpion() function with a URL for the "cuponscorpion" website to continue scraping coupon codes.
Once all the coupon codes have been scraped and added to the global lists, the script calls the printer() function to write the information to the "output.csv" file using the csv module. The function writes the scraped information to the file row by row, with each row representing a single course and containing the course name, course link, coupon code, and expiration date.
Overall, this code scrapes Udemy coupon codes from various websites using Selenium and/or BeautifulSoup and writes the information to a CSV file. The script is set up to scrape from multiple websites in case there are not enough coupon codes scraped from the first website.






















