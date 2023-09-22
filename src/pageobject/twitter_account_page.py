from typing import Self

from playwright.sync_api import Page

from src.pageobject.base.base_page import BasePage
from src.pageobject.widgets.turn_on_notifications_widget import (
    TurnOnNotificationsWidget,
)


class TwitterAccountPage(BasePage):
    """Twitter Profile Page. Stores all the logic to work with tweets"""

    def __init__(self, page: Page):
        self.tweets_selector = 'div[data-testid="tweetText"]'
        self.notifications_widget = TurnOnNotificationsWidget(page)

        super().__init__(page)

    def open(self, usertag: str) -> Self:
        """Navigates directly to the usertag page, then closes the notifications pop-up."""
        self.navigate_to_url(usertag)
        self.notifications_widget.close_widget()
        return self

    def get_recent_tweets(self, count=10):
        """
        Returns the specified amount of recent tweets' texts. Default value is 10.
        Scrolls through the page until the amount of unique tweets in tweet_texts is less than expected amount.
        During each iteration, additional waiting for page to load content is added.
        """
        tweet_texts = set()
        last_seen_tweets = set()

        while len(tweet_texts) < count:
            tweets = self.get_elements_list(self.tweets_selector)
            new_tweets = [t for t in tweets if t.text_content() not in last_seen_tweets]

            for t in new_tweets:
                text = t.text_content()
                tweet_texts.add(text)

            self.scroll_page_down()
            last_seen_tweets = set([t.text_content() for t in tweets])

        return tweet_texts
