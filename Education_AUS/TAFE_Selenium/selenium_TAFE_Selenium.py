from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time  # Importing time module for pauses

# List of keywords for search
keywords = [
    "management", "medical", "engineering", "nail"
]

# Setup the Edge service
service = Service(EdgeChromiumDriverManager().install())

# Initialize the Edge driver
driver = webdriver.Edge(service=service)

# General counter for all keywords
total_records = 0

for keyword in keywords:
    driver.get(f"https://tafeqld.edu.au/search-results?searchterm={keyword}&region=&type=courses")
    
    time.sleep(2)  # Pausing for 2 seconds after loading the page

    # Extracting course details
    course_titles = driver.find_elements(By.XPATH, "//h3[@class='cmp-custom-courses-results-card__container-details-title']")
    course_durations = driver.find_elements(By.XPATH, "//div[@class='cmp-custom-courses-results-card__container-details-slotsection-duration']")
    course_start_dates = driver.find_elements(By.XPATH, "//div[@class='cmp-custom-courses-results-card__container-details-slotsection-startdate']")
    course_lists = driver.find_elements(By.XPATH, "//ul[@class='cmp-custom-courses-results-card__container-listsection-list']")
    course_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/course/')]")
    
    keyword_records = len(course_titles)  # Counter for the current keyword
    total_records += keyword_records  # Updating the general counter
    
    print(f"Results for keyword: {keyword}")
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    for i in range(len(course_titles)):
        title = course_titles[i].text if i < len(course_titles) else 'N/A'
        duration = course_durations[i].text if i < len(course_durations) else 'N/A'
        start_date = course_start_dates[i].text if i < len(course_start_dates) else 'N/A'
        link = course_links[i].get_attribute('href') if i < len(course_links) else 'N/A'
        
        print(f"Title: {title}")
        print(f"Duration: {duration}")
        print(f"Start Date: {start_date}")
        print(f"Link: {link}")
        
        if i < len(course_lists):
            list_items = course_lists[i].find_elements(By.TAG_NAME, "li")
            for item in list_items:
                print(f"Relevant Field: {item.text}")
        print("-------------------------------------------------------------------------------")
    
    print(f"Total records for {keyword}: {keyword_records}")
    time.sleep(2)  # Pausing for 2 seconds after completing the search for each keyword
    print("\n\n")

print(f"Total number of records extracted for all keywords: {total_records}")

# Close the browser
driver.quit()
