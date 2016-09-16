tabby_cat = "%sI'm %s in."
persian_cat = "I'm %s%son a line."
backslash_cat = "I'm %s a %s %s."

fat_cat = """
I'll do a list:
%s* %s
%s* %s
%s* %s
"""

print tabby_cat % ("\t", "tabbed")
print persian_cat % ("split", "\n")
print backslash_cat % ("\\", "\\", "cat")
print fat_cat % ("\t", "cat food", "\t", "fish", "\t", "cat litter")

