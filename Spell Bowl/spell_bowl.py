import requests


white = "\033[0m"
red = "\033[91m"
cyan = "\033[36;1m"

key = "b13f77db-af02-4487-a533-ad365ce54021"

# initialze a list of words from file
with open("list.txt", "rt") as f:
    words = f.read()
    words = words.split("\n")[240:]
    f.close()

# print(words[:4])

#shortdef
#fl = part of speach

error_count = 0
word_count = 0


with open("results.txt", "a") as file:

    while error_count <= 5 and word_count < len(words):
        try:
            word = words[word_count]

            if word_count % 75 == 0:
                print(f"{word_count} out of {len(words)} | {word}")

            api_url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=b13f77db-af02-4487-a533-ad365ce54021"
            response = requests.get(api_url).json()[0]  # to access the inner dictionary


            # speech_part = response["fl"]

            # takes the first defininition
            define = response["shortdef"][0] # to prevent the list formatting

            file.write(f"{word} <break> {define}\n")
            word_count += 1

        except Exception as err:
            print(red, f"[ ERROR ] {type(err).__name__} was raised: {err}", white)
            error_count += 1


print(f"\n\nCollected {word_count} word(s). {len(words) - word_count} remaining.")

with open("temp.txt", "r+") as f:
    f.writelines("\n".join(words[word_count:]))

print("~~~~~~~~~DONE~~~~~~~~~")

