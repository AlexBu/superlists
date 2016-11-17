from selenium import webdriver

browser = webdriver.Firefox()

# Alex has heard about a cool new online to-do app.
# He goes to check out its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# He is invited to enter a to-do item straight away

# He types "Buy MacBookPro" into a text box

# When he hits enter, the page updates, and now the page lists
# "1: Buy MacBookPro" as an item in a to-do list

# There is still a text box inviting him to add another item.
# He enters "Use MacBookPro to make an app"

# The page updates again, and now shows both items on his list

# Alex wonders whether the site will remember his list. Then
# he sees that the site has generated a unique URL for him --
# there is some explanatory text to that effect.

# He visits that URL - his to-do list is still there.

# Satisfied, he goes back to sleep

browser.quit()
