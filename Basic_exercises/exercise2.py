text = "  Hello, World! Welcome to Python Programming.  "

text_strp = text.strip()
print("Stripped:",text_strp)
new_text = text.split()
print("Word count:",len(new_text))
print("Title case:",text_strp.title())
print("Starts with Hello:",text_strp.startswith("Hello"))
print("Starts with Hello:",text_strp.endswith("ing."))
print("Python position:",text_strp.find("Python"))
print("Joined:","-".join(new_text))


