import re
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get("https://onlinegpt.org/")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Type your message...'][@maxlength='512']"))
        )

        inputfield = driver.find_element(By.XPATH, "//textarea[@placeholder='Type your message...'][@maxlength='512']")
        sendbutton = driver.find_element(By.XPATH, "//button[./span[text()='Send']]")
        user_input = request.json.get('user_input')
        delimiter_statement = "Enclose your response in 3 dollar signs like so: $$$Example Response$$$"
        
        if user_input.lower() == "exit":
            driver.quit()
            return jsonify({"AI": "Goodbye!"})

        prompt = user_input + delimiter_statement
        inputfield.click()
        inputfield.send_keys(prompt)
        sendbutton.click()

        time.sleep(7)

        reply_divs = driver.find_elements(By.CLASS_NAME, "mwai-ai")
        ai_response = []

        for reply_div in reply_divs:
            text_content = reply_div.text
            
            start_pos = text_content.find('$$$')
            end_pos = text_content.rfind('$$$')
            
            if start_pos != -1 and end_pos != -1:
                useful_text = text_content[start_pos + 3:end_pos].strip()
                
                ai_response.append(useful_text)
            
        return jsonify({"AI": ai_response})
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}") 

    finally:
        # Ensure that the WebDriver instance is always quit, even on exceptions
        if 'driver' in locals():
            driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
