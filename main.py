### this file contains the Cohere API

import cohere

co = cohere.ClientV2(api_key="PraIz8Li2iWpv3xDsd1UsIfvY0ZkVfcWv7dgmFsl")

# obtain text (i.e.receipt or list of food items)

res = co.chat(
    model="command-r-plus-08-2024",
    messages=[
        {
            "role": "user",
            "content": "Using the following food items, do two things. " + "" # food items
                       "First, use online search to give an estimation of each item's expiry date. "
                       "Second, suggest for the items which exire in the next 3 days, "
                       "a recipe that can be made using all of them. \n\n",
        }
    ],
)

print(res.message.content[0].text)
