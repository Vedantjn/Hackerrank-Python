regex_pattern = r"\D+"
# regex_pattern = r"[.,]+"
	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))