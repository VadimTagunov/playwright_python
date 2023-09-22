from playwright.sync_api import Locator

from src.elements.base.base_element import BaseElement


class Button(BaseElement):
    """Wrapper on button elements for the UI. Should contain button-specific methods (disabled / enabled etc.)."""

    def __init__(self, locator: Locator):
        super().__init__(locator)
