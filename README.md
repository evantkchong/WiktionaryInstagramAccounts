# Wiktionary Instagram Accounts

A simple scraping project to identify available usernames on Instagram, using [*english Wiktionary*](https://en.wiktionary.org/wiki/Wiktionary:Main_Page) as a resource of usernames.

If you want to, you could replace the Wiktionary Dump file with your own reference material as a resource of usernames to look up.

## Project Status
This project is a currently a work in progress. The main challenge preventing me from completing this right now is that I'm relying on making a HTTPS GET request to https://www.instagram.com/{username}/?__a=1 and using the returned status code to determine if the username has already been taken or not.

While this approach has a higher limit rate than using the Instagram developer API, it still has it's limitations and I am only able to make around `50000` requests in a span of `4 hours` before being kicked out. This is even with implementing retries with a high backoff factor.

Work is being done to:
1. Make it easier to pick off where we left off after being kicked out
2. Find a more robust way to determine username availability

## Acknowledgments

- Wiktionary article titles made available through [*Wikimedia Dumps*](https://dumps.wikimedia.org/backup-index.html)
