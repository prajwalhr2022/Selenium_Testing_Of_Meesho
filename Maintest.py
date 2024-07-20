import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = uc.Chrome()
def test_click_view_all(driver):
    try:
        # Wait for the Women Ethnic section to be present
        women_ethnic_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[1]"))
        )
        # Hover over the Women Ethnic section to reveal the "View All" button
        ActionChains(driver).move_to_element(women_ethnic_section).perform()
        time.sleep(2)  # Allow some time for the hover effect
        # Wait for the "View All" button to be present and clickable
        view_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div.DesktopHeader__HeaderStyled-sc-r0p6o1-0.bRUKyL > div:nth-child(4) > div > div:nth-child(2) > div > div:nth-child(1) > a > p'))
        )
        view_all_button.click()
        print("women ethnic section Successful.")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_tops(driver):
    try:
        # Wait for the Women Western section to be present
        women_western_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[3]/span"))
        )

        # Hover over the Women Western section to reveal the 'Tops' button
        ActionChains(driver).move_to_element(women_western_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'Tops' button to be present and clickable
        tops_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[4]/div/div[1]/a[1]/p"))
        )
        tops_button.click()
        print("women western section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_men_accessories(driver):
    try:
        # Wait for the Men section to be present
        men_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Men']"))
        )

        # Hover over the Men section to reveal the 'All Men Accessories' button
        ActionChains(driver).move_to_element(men_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'All Men Accessories' button to be present and clickable
        men_accessories_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[6]/div/div[3]/a[1]/p"))
        )
        men_accessories_button.click()
        print("Men section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_baby_care(driver):
    try:
        # Wait for the Kids section to be present
        kids_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Kids']"))
        )

        # Hover over the Kids section to reveal the 'All Baby Care' button
        ActionChains(driver).move_to_element(kids_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'All Baby Care' button to be present and clickable
        baby_care_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[8]/div/div[4]/a/p"))
        )
        baby_care_button.click()
        print("kids section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_kitchen_storage(driver):
    try:
        # Wait for the Home & Kitchen section to be present
        home_kitchen_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Home & Kitchen']"))
        )

        # Hover over the Home & Kitchen section to reveal the 'Kitchen Storage' button
        ActionChains(driver).move_to_element(home_kitchen_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'Kitchen Storage' button to be present and clickable
        kitchen_storage_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[10]/div/div[3]/a[1]/p"))
        )
        kitchen_storage_button.click()
        print("Kitchen&Storage section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_deodorants(driver):
    try:
        # Wait for the Beauty & Health section to be present
        beauty_health_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Beauty & Health']"))
        )

        # Hover over the Beauty & Health section to reveal the 'Deodorants' button
        ActionChains(driver).move_to_element(beauty_health_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'Deodorants' button to be present and clickable
        deodorants_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[12]/div/div[3]/a/p"))
        )
        deodorants_button.click()
        print("Beauty section Successful.")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_jewellery_set(driver):
    try:
        # Wait for the Jewellery & Accessories section to be present
        jewellery_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Jewellery & Accessories']"))
        )

        # Hover over the Jewellery & Accessories section to reveal the 'Jewellery Set' button
        ActionChains(driver).move_to_element(jewellery_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'Jewellery Set' button to be present and clickable
        jewellery_set_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[14]/div/div[1]/a[1]/p"))
        )
        jewellery_set_button.click()
        print("Jewellery section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_all_men_bags(driver):
    try:
        # Wait for the Bags & Footwear section to be present
        bags_footwear_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Bags & Footwear']"))
        )

        # Hover over the Bags & Footwear section to reveal the 'All Men Bags' button
        ActionChains(driver).move_to_element(bags_footwear_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'All Men Bags' button to be present and clickable
        all_men_bags_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[16]/div/div[2]/a[1]/p"))
        )
        all_men_bags_button.click()
        print("Bags section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_all_appliances(driver):
    try:
        # Wait for the Electronics section to be present
        electronics_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Electronics']"))
        )

        # Hover over the Electronics section to reveal the 'All Appliances' button
        ActionChains(driver).move_to_element(electronics_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'All Appliances' button to be present and clickable
        all_appliances_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[18]/div/div[2]/a[1]/p"))
        )
        all_appliances_button.click()
        print("Electronic section Successful")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_search_functionality(driver):
    try:
        # Wait for the search input to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-input-elm"))
        )
        search_box.send_keys("Saree")
        search_box.send_keys(Keys.RETURN)

        # Wait for the products to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ProductList__PLPContainer-sc-8lnc8o-1"))
        )

        # Print statement to indicate execution
        print("Products searched successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def test_select_download_app(driver):
    try:
        # Wait for the "Download App" button to be present
        download_app_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[1]"))
        )
        time.sleep(2)  # Delay to see the button

        # Click the "Download App" button
        download_app_button.click()
        print("Download App button clicked.")
        time.sleep(1)  # Delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_select_become_supplier(driver):
    try:
        # Wait for the "Become a Supplier" button to be present
        become_supplier_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[3]/span"))
        )
        time.sleep(2)  # Delay to see the button

        # Click the "Become a Supplier" button
        become_supplier_button.click()
        time.sleep(1)  # Delay to see the result of the click
        print("BecomeSupplier Test Successful")
    except Exception as e:
        print(f"An error occurred: {e}")
def search_and_select_saree(driver):

    try:
        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Try Saree, Kurti or Search by Product Code']"))
        )
        print("Search box found. Entering 'Saree' and submitting search.")

        # Enter 'Saree' in the search box and simulate pressing Enter
        search_box.send_keys("Saree")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[3]/div/div[3]"))
        )

        # Wait for the checkbox in the category section to be present
        print("Waiting for the saree checkbox in the category section...")
        saree_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#__next > div.sc-ftTHYK.cRaSHh > div > div:nth-child(3) > div.sc-dkrFOg.DeskopSortFilterStyled__StyledCol-sc-18gw3z1-0.fwLbyR.bjIHSf > div > div.sc-ftTHYK.jfdUoi.DeskopSortFilterStyled__FilterWrapper-sc-18gw3z1-2.fobakx.DeskopSortFilterStyled__FilterWrapper-sc-18gw3z1-2.fobakx > div:nth-child(4) > div:nth-child(1) > div.sc-kDvujY.dKxUIu > div.sc-eDWCr.dgzSQI > div > div > div > span:nth-child(1) > svg"))
        )

        # Click the saree checkbox
        saree_checkbox.click()
        print("Saree checkbox clicked.")
        time.sleep(1)  # Small delay to see the result
    except Exception as e:
        print(f"An error occurred: {e}")
def search_and_apply_filter(driver):
    try:
        # Wait for the search box to be present and search for 'Saree'
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Try Saree, Kurti or Search by Product Code']"))
        )
        search_box.send_keys("Saree")
        search_box.send_keys(Keys.RETURN)

        # Wait for the page to load search results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ProductList__PLPContainer-sc-8lnc8o-1"))
        )

        # Wait for the dropdown button to be visible and click it using ActionChains
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#__next > div.sc-ftTHYK.cRaSHh > div > div:nth-child(3) > div.sc-dkrFOg.DeskopSortFilterStyled__StyledCol-sc-18gw3z1-0.fwLbyR.bjIHSf > div > div.sc-ftTHYK.eHVGcU.DeskopSortFilterStyled__SortWrapper-sc-18gw3z1-1.ezlkPE.DeskopSortFilterStyled__SortWrapper-sc-18gw3z1-1.ezlkPE > ul > li > div.Selectstyled__DropDownSelected-sc-j3bykl-2.exOamp > svg"))
        )
        ActionChains(driver).move_to_element(dropdown_button).click().perform()

        # Wait for the 'Price(High to Low)' option to be visible and click it
        price_high_to_low_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[text()='Price (High to Low)']"))
        )
        ActionChains(driver).move_to_element(price_high_to_low_option).click().perform()

        print("Filter applied: Sorted by Price(High to Low).")

        time.sleep(1)  # Small delay to see the result of the filter

    except Exception as e:
        print(f"An error occurred: {e}")

def test_click_newsroom(driver):
    try:

        newsroom_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[5]"))
        )
        time.sleep(2)  # Small delay to see the button
        newsroom_button.click()
        time.sleep(1)  # Small delay to see the result of the click
        print("Newsroom Clicked")

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_sign_up_button(driver):
    try:
        # Wait for the profile section to be present
        profile_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[7]"))
        )
        ActionChains(driver).move_to_element(profile_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Click on the Sign Up button
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[7]/div/div/button/div/span")
            )
        )
        sign_up_button.click()
        print("Sign Up button clicked.")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_my_orders(driver):
    try:
        # Wait for the Profile section to be present
        profile_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Profile']"))
        )

        # Hover over the Profile section to reveal the 'My Orders' button
        ActionChains(driver).move_to_element(profile_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'My Orders' button to be present and clickable
        my_orders_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[7]/div/div/a[1]/div/span"))
        )
        my_orders_button.click()
        print("My Orders button clicked.")

        time.sleep(1)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_account(driver):
    try:
        # Wait for the profile section to be present
        print("Waiting for the profile section...")
        profile_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[7]"))
        )
        print("Profile section found. Hovering over it.")

        # Hover over the profile section
        actions = ActionChains(driver)
        actions.move_to_element(profile_section).perform()

        # Wait for the 'Delete Account' button to be visible
        print("Waiting for the 'Delete Account' button to be visible...")
        delete_account_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[2]/div[1]/div/div[3]/div[7]/div/div/a[2]/div/span"))
        )

        # Click the 'Delete Account' button
        print("Delete Account button found. Clicking it.")
        delete_account_button.click()

        print("Delete Account button clicked.")

        time.sleep(1)  # Small delay to see the result

    except Exception as e:
        print(f"An error occurred: {e}")
def test_click_cart_button(driver):
    try:
        # Wait for the cart button to be present and clickable
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Cart')]"))
        )
        cart_button.click()
        print("Cart button clicked.")

        time.sleep(2)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
def go_to_homepage(driver):
    driver.get("https://www.meesho.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Women Ethnic')]")))
    time.sleep(2)  # Ensure the page loads completely



def main():
    driver = uc.Chrome()
    try:
        driver.get("https://www.meesho.com/")
        test_click_view_all(driver)
        go_to_homepage(driver)
        test_click_tops(driver)
        go_to_homepage(driver)
        test_click_men_accessories(driver)
        go_to_homepage(driver)
        test_click_baby_care(driver)
        go_to_homepage(driver)
        test_click_kitchen_storage(driver)
        go_to_homepage(driver)
        test_click_deodorants(driver)
        go_to_homepage(driver)
        test_click_jewellery_set(driver)
        go_to_homepage(driver)
        test_click_all_men_bags(driver)
        go_to_homepage(driver)
        test_click_all_appliances(driver)
        go_to_homepage(driver)
        test_search_functionality(driver)
        go_to_homepage(driver)
        test_select_download_app(driver)
        go_to_homepage(driver)
        test_select_become_supplier(driver)
        go_to_homepage(driver)
        search_and_select_saree(driver)
        go_to_homepage(driver)
        search_and_apply_filter(driver)
        go_to_homepage(driver)
        test_click_newsroom(driver)
        go_to_homepage(driver)
        test_click_sign_up_button(driver)
        go_to_homepage(driver)
        test_click_my_orders(driver)
        go_to_homepage(driver)
        delete_account(driver)
        go_to_homepage(driver)
        test_click_cart_button(driver)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if driver:
            driver.quit()
            print("Driver quit successfully.")


if __name__ == "__main__":
    main()
