# Enter script code

import re

contents = clipboard.get_selection()

lower_case = contents.lower()

domain_match = re.match(r'''^\s*(https?://)?([a-z0-9._-]+)''', lower_case)

if domain_match:
    domain = domain_match.groups()[1]
    
   
    # Until clipboard.fill_selection() is fixed
    system.exec_command("echo -n '%s' | xclip -i" % domain)
    