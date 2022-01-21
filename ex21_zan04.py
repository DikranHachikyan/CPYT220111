
if __name__ == '__main__':
#   
    users = ['anna', 'maria', 'markus', 'jorg', 'florian']
    mails = ['anna@no.com', 'maria@no.com', 'markus@no.com', 'jorg@no.com']

    for data in zip(users, mails):
        name, mail = data
        print(f'data = {data} name= {name} => {mail}')
   
    print('---')