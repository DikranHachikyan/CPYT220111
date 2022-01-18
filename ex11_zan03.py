def new_file():
    return 'Create a new file...'

def open_file():
    return 'Open file ...'

def save_file():
    return 'Save file ...'

def quit_app():
    print('Quit App')
    quit()

# ----------------------------

actions = {
    'n':new_file,
    'p':open_file,
    's':save_file,
    'q':quit_app
}


ch = input('Command (n-new, p-open, s-save, q-quit):')

if ch in actions:
    res = actions[ch]()
    print(f'result:{res}')
else:
    print(f'Unknown Command:{ch}')

print('---')