# Paging mechanism

Some methods returning a list of items are using a paging mechanism.

The GroupCamp API uses two kinds of paging mechanism.

# The 'next' mechanism

In the `next` mechanism, after fetching the first page, the methods
determines there are more items to fetch, and provides in the answer
an URL to call to fetch the next page. Using that method, items are
fetched for every call, the result may be modified between two
calls. E.g. if there are 105 items, and the first call send the first
100, when fetching for the next page, if the 5 remaining items have
been deleted, the page will be empty.

This mechanism is usualy used when the update risk is void, or very
low, like for fetching the messages in a discussion thread, or when
fetching all the items may slow down the system.

In the `next` mechanism, the answer is a JSON object with the
following fields:

Name      | Type   | Description
----------|--------|------------------------------
result    | Array  | The items in the page (type according to the called method).
next_page | String | URL to call to fetch the next page.

# The 'full' mechanism

In the `full` mechanism, all the items are fetched, and stored. Thus
the mechanism can provide more informations, like the exact number of
pages. The pages are available for a maximum of 24 hours in a cache
(can be less when the cache is cleared). When an expired page is
fetched, a specific error is returned : `Gone`, with HTTP status 410.

In the `full` mechanism, the answer is a JSON object with the following
fields:

Name          | Type    | Description
--------------|---------|-------------------------
result        | Array   | The items in the page (type according to the called method).
next_page     | String  | URL to call to fetch the next page, when available.
previous_page | String  | URL to call to fetch the previous page, when available.
page_count    | Integer | The number of pages.
current_page  | Integer | The current page number.
