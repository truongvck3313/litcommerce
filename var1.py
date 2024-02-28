from selenium.webdriver.common.by import By



PATH ="C:/Users/Admin/PycharmProjects/pythonProject/chromedriver.exe"
file_name = 'C:/Users/Admin/PycharmProjects/pythonProject/litcommerce/data_litcommerce1.json'
url = "https://app.litcommerce.com/login?redirect=/first-setup/setup-source-cart"




login_user = "//*[@name='email']"
login_password ="//*[@name='password']"
login_submit = "//*[text()='Sign in now']"
icon_lit = "//*[@src='/static/logo-litcommerce.svg']"
icon_x = "//*[@aria-label='close']"

shopify_order = By.XPATH,"//*[text()='Orders']"
shopify_addorder = By.XPATH,"//*[text()='Create order']"
tiktok_order = By.XPATH,"//*[text()='Orders']"
tiktok_managereturn = By.XPATH,"//*[text()='Manage Returns']"
