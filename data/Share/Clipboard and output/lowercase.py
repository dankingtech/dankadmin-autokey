contents = clipboard.get_selection()

lower_case = contents.lower()

# Until clipboard.fill_selection() is fixed
system.exec_command("echo -n '%s' | xclip -i" % lower_case)
