contents = clipboard.get_selection()

collapsed = " ".join(contents.split("\n"))

#keyboard.send_keys(collapsed)

# Until clipboard.fill_selection() is fixed
system.exec_command("echo -n '%s' | xclip -i" % collapsed)
