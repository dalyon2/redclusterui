## Synopsis

The user requests a year and month, then flask requests the data from the database and hands it off to d3.js for display.
d3.JS creates a force directed graph given a list of (subredditName, clusterID, subredditSize). Hovering the mouse over a subreddit
displays its name in a tooltip. Currently, the scaling is set to 1 pixel = 400 posts/month. Ideally, the scale should be passed as a parameter from the database.

## Motivation

I wanted to visualize how Reddit users are clustered to see if we're really all living in tiny bubbles.
