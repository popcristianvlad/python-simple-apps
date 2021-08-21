from googletrans import Translator

translater = Translator()

out = translater.translate("Hello. How are you ?", dest="ro")

print(out)
print(out.text)
