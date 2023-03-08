# SecondTask_CAS

  ## Udemy Course Cupon Scraper Task 


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
 
 

  
























