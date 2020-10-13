import pytest


@pytest.mark.usefixtures("setup")
class TestExampleTwo:

    def test_simpleInputForm(self):

        print("Another example")
        mainMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Input Forms')]")
        mainMenu.click()

        subMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Simple Form Demo')]")
        subMenu.click()

        #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = self.driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Test Python")

        #Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn=self.driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()

        #Checking whether the input text and output text are same using assertion.
        eleYourMsg=self.driver.find_element_by_id("display")
        assert "Test Python" in eleYourMsg.text
