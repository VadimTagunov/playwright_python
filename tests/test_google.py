import pytest

from src.pageobject.twitter_account_page import TwitterAccountPage
from src.utils.tweet_analysis import TweetAnalyzer


@pytest.mark.parametrize("amount", [100])
def test_something(page, amount):
    """
    Test opens Google account on Twitter in incognito mode,
    scans for last {amount} of tweets,
    asserts that received amount is bigger than or equal to expected {amount},
    and then prints the statistics.

    It doesn't support headless mode, as Twitter blocks headless browsers with the "This browser is no longed supported"
    The only option is headed mode, which is set in config.json.
    """
    tweets = TwitterAccountPage(page).open("Google").get_recent_tweets(count=amount)

    assert len(tweets) >= amount, f"Unable to get {amount} last unique tweets."

    TweetAnalyzer.print_statistics(tweets)
