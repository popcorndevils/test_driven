from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:8000")

assert "install" in browser.title
print("yeah")
