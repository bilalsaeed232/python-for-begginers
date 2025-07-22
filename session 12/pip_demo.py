# Program: Google Translator

import asyncio
from googletrans import Translator

async def main():
    translator = Translator()

    while True:
        print("1. German")
        print("2. Urdu")
        print("3. French")
        print("4. Spanish")
        print("5. Russian")
        print("6. Italian")

        choice = input("Which language you want to translate to ('0' to exit)?")
        text = input("Enter your text:")

        language_code = "en"
        match choice:
            case "1":
                language_code = "de"
            case "2":
                language_code = "ur"
            case "3":
                language_code = "fr"
            case "4":
                language_code = "es"
            case "5":
                language_code = "ru"
            case "6":
                language_code = "it"
            case "0":
                break

        translated = await translator.translate(text, dest=language_code)  # await here

        print("Original:", text)
        print("Translated:", translated.text)
        

asyncio.run(main())

