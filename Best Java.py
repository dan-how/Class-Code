string = "We will be the best Java Developers the world has ever seen!"
new_string = string.replace('Java Developers', 'Cloud Engineers')
ce = new_string[20:35]
shout = ce.upper()
final_string = ' '.join(reversed(shout))

print(final_string)
print(new_string)