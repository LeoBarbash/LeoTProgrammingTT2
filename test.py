file = open(f'dev.py',  'r', encoding='utf-8')
content = file.readlines()
button = 0
for line in content:
    if line[7:27] == 'Hello world from dev':
        print('Statement is correct')
        button = 1
if button == 0:
    print('Incorrect statement!')
