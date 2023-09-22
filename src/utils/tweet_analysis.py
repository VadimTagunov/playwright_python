class TweetAnalyzer:
    """
    Class that contains logic on analysing tweets and printing the appropriate statistics.
    """

    @staticmethod
    def print_statistics(tweets):
        """Prints all the tweets provided, as well as the amount of mentions and hashtags"""
        mentions = {}
        hashtags = {}

        print("\nReceived tweets:")
        for i, tweet in enumerate(list(tweets)):
            print(f"{i + 1}. {tweet}")

        for tweet in tweets:
            for word in tweet.split():
                if word.startswith("@"):
                    mentions[word] = mentions.get(word, 0) + 1
                if word.startswith("#"):
                    hashtags[word] = hashtags.get(word, 0) + 1

        print("\nMentions:")
        for mention, amount in mentions.items():
            print(f"{mention} -> {amount} time(s)")

        print("\nHashtags:")
        for hashtag, amount in hashtags.items():
            print(f"{hashtag} -> {amount} time(s)")
