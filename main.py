# This is a simple Python script to convert text into handwriting.
# Copyright (c) 2022 Vaibhav Ganeriwala

# import the required modules
import pywhatkit as kit

# get the text from the user
text = input("Enter the text that you wish to convert to Handwriting : ")

# main function
def text_to_handwriting(text):
    """Convert the text to Handwriting"""
    kit.text_to_handwriting(text, rgb=[0, 0, 138])
    print("Converting to Handwriting...")
    print("Done!")

# call the function
text_to_handwriting(text)