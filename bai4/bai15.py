import re

txt = "My son is 3 years and 8 months old"
numbers = re.findall("\d+", txt)
txt_out = "".join(numbers)
print(txt_out)