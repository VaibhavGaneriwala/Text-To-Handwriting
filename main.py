import pywhatkit as kit

text = input("Enter the text that you wish to convert to Handwriting : ")
print("Converting to Handwriting...")
kit.text_to_handwriting(text, rgb=[0, 0, 138])
print("Done!")