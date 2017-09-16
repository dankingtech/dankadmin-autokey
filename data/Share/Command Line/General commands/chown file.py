contents = clipboard.get_selection()
match = re.search(r"^/home/(?P<user>[a-z0-9]+)[a-zA-Z0-9._/-]*$", contents)
if match is not None:
  keyboard.send_keys("chown {0}:{0} {1}".format(match.group('user'), contents))
else:
  dialog.info_dialog("chown file", "Not a valid file for auto chown: {}".format(contents))
