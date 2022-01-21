
if __name__ == '__main__':
#   
    config = {
        'title':'Text Editor',
        'version':'1.2',
        'n_proc': 10,
        'max_mem':4096,
        'margins':[5,10,10,5]
    }

    for key,value in config.items():
        print(f'{key} => {value} ')
        

   
    print('---')