from selenium import webdriver
import urllib.request
import os

# Configure Selenium webdriver
driver = webdriver.Chrome()  # Change this path to the location of your chromedriver executable

# Open the webpage
driver.get("https://www.google.com/search?q=pashupatinath&tbm=isch&sa=X&ved=2ahUKEwiCr-DBg97_AhUl-jgGHX1JDFMQ0pQJegQICxAB&biw=1536&bih=792&dpr=1.25")  # Replace with the URL of the webpage you want to scrape images from

# Specify the folder path to save the images
folder_path = "images"  # Replace with the desired folder path

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Find all image elements on the webpage
root_element = driver.find_element_by_tag_name('body')
image_elements = root_element.find_elements_by_tag_name('img')

# Download and save each image to the specified folder
for index, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute('src')
    image_name = f"image_{index}.jpg"  # You can modify the filename as per your requirement

    # Download the image
    image_path = os.path.join(folder_path, image_name)
    urllib.request.urlretrieve(image_url, image_path)
    print(f"Image {index + 1} saved at {image_path}.")

# Close the browser
driver.quit()
