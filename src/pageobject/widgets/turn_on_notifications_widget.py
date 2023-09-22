from playwright.sync_api import Page

from src.elements.button import Button
from src.pageobject.base.base_page import BasePage


class TurnOnNotificationsWidget(BasePage):
    """
    Widget that appears when opening account page in incognito mode.
    A temporary workaround to not block the scenario.

    Initially, the idea was to either set a proper cookie so that this widget is not shown, or
    handle the event causing this widget to appear. But because it's a custom and not build-in
    widget, it's hard to find the root cause of appearing, so leaving it as a workaround.
    """

    def __init__(self, page: Page):
        self.__close_btn = Button(page.locator("div[data-testid='app-bar-close']"))
        self.__turn_on_notifications_btn = Button(
            page.get_by_text("Turn on notifications")
        )
        self.__not_now_btn = Button(page.get_by_text("Not now"))
        super().__init__(page)

    def close_widget(self):
        """Close widget by clicking [X] icon"""
        self.__close_btn.click()

    def accept_notifications(self):
        """Close widget by accepting notifications"""
        self.__turn_on_notifications_btn.click()

    def discard_notifications(self):
        """Close widget by declining notifications"""
        self.__not_now_btn.click()
