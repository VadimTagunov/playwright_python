from playwright.sync_api import Locator


class BaseElement:
    """
    A class that should be parent for all of the elements which SDET will interact during Page Object creation.
    Children that are extending this class should be stored as a private fields of the Page class.
    """

    def __init__(self, locator: Locator):
        self.locator = locator

    def click(self):
        """Clicks the element"""
        self.locator.click()

    def get_text(self) -> str:
        """Returns the element text content as a string"""
        return self.locator.text_content()
