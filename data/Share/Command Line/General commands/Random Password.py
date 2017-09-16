output = system.exec_command("head -c 100 /dev/urandom | tr -dc '_A-Za-z0-9.*@#%' |head -c 12")
keyboard.send_keys(output)