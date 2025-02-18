import cohere
from read_receipt import read

co = cohere.ClientV2(api_key="")

# Obtaining all foods from a receipt
def filter_receipt(path):
    text = read(path)
    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role": "user",
                "content": "You will be given the text contents of a receipt. You are to only obtain the names of foods listed on the receipt."
                "You will list them all separated by a comma. Here is the text: " + text,
            }
        ],
    )
    return res.message.content[0].text
print(filter_receipt('test/receipt_1.jpeg'))

# Determine expiry date of food items
def expiry(is_receipt, img):
    if is_receipt:
        food = filter_receipt(img)
    else:
        food = filter_image(img)

    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role": "user",
                "content": "Using the following food items, use online search to give an estimation of each item's expiry date. "
                           "Do not include any bullet points. Only include the name of the food, and the expiry date in days, separated by a comma."
                           "Do not include any other information. Sort the items from lowest expiry date to highest. "
                           "Here are the food items: " + food,
            }
        ],
    )
    return res.message.content[0].text
print(expiry(True, 'test/receipt_1.jpeg'))

# Obtain recipe for foods
def recipe(txt):
    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role": "user",
                "content": "Using the following food items, give me 6 different recipes using the food items close to expiry."
                           "Here is the food items and their expiry dates. "+ txt,
            }
        ],
    )
    return res.message.content[0].text
print(recipe(expiry(True, 'test/receipt_1.jpeg')))
