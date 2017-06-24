from settings import COMMAND_PREFIX

def remove_command(command):
    if (command[0] == COMMAND_PREFIX):
        i = 0
        for c in command:
            if c == ' ':
                i += 1
                break
            else:
                i += 1
        command = list(command)
        del command[:i]
        command = ''.join(command)
        return command

def remove_until_newline(text):
    i = 0
    for c in text:
        if c != '\n':
            i += 1
        else:
            i += 1
            break
    text = list(text)
    del text[:i]
    text = ''.join(text)
    return text


