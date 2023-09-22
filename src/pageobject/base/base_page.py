from playwright.sync_api import Page, ElementHandle


class BasePage:
    """Parent for all the pages in PageObject model. Contains very common behaviour for each web page"""

    BASE_TIMEOUT: float = 500

    def __init__(self, page: Page):
        self._page = page

    def navigate_to_url(self, url: str):
        """Opens provided url"""
        self._page.goto(url)

    def wait_for_load(self):
        """Waits for load state"""
        self._page.wait_for_load_state("load")

    def wait_for_networkidle(self):
        """Waits for networkidle state"""
        self._page.wait_for_load_state("networkidle")

    def wait_for_domcontentloaded(self):
        """Waits for domcontentloaded state"""
        self._page.wait_for_load_state("domcontentloaded")

    def wait_for_full_load(self):
        """Waits for all available handled states"""
        self.wait_for_domcontentloaded()
        self.wait_for_load()
        self.wait_for_networkidle()

    def scroll_page_down(self, wait_required=True):
        """Scrolls page by simulating mouse wheel movement. By default, additionally waits for timeout after scroll"""
        self._page.mouse.wheel(
            delta_x=0, delta_y=self._page.viewport_size["height"] / 2
        )
        if wait_required:
            self._page.wait_for_timeout(self.BASE_TIMEOUT)

    def get_elements_list(self, selector) -> list[ElementHandle]:
        """Returns the list of ElementHandle objects by provided string selector"""
        return self._page.query_selector_all(selector)
