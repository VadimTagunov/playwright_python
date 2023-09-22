import json
import pytest

from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def config():
    """Returns parsed configuration from json file"""
    with open("config.json") as config_file:
        config = json.load(config_file)

    return config


@pytest.fixture(scope="function")
def page(config) -> Page:
    """
    Setup / teardown for each test: yields the page for testing, then closes current context and browser.
    Initially, only Chrome supported with a way to extend it.
    """
    with sync_playwright() as p:
        if config["browser"] == "Chrome":
            b = p.chromium.launch(headless=config["headless"])
        else:
            raise Exception(f"Browser '{config['browser']}' is not supported")

        context = b.new_context(
            base_url=config["base_url"],
            viewport={"width": config["width"], "height": config["height"]},
        )

        yield context.new_page()

        context.close()
        b.close()
