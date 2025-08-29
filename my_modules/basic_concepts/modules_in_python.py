import math
import mymodule
import requests

# 2 types of modules
# 1: built in modules --> provided by python -->
#       example math ftplib-->
#       List of all built in modules: https://docs.python.org/3/py-modindex.html
# 2: external modules --> Downloaded by pip. Custom modules. example: django/openai/ functions py that you wrote in this project can be treated as a custom module


# Built in
print(math.sqrt(16))

print(math.sqrt.__doc__)

# My Custom
mymodule.greetings("I Will nail Python!!")

# From Pip, we downloaded requests and not trying it out

response = requests.get("https://www.google.com").text
print(response)
