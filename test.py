while True:
    print('To exit, type "exit".')
    print('Please type file name')
    
    file_name = input('= ')
    
    if file_name == "exit":
        break
    else:
        print(f"{{{{ url_for('static', filename='css/{file_name}') }}}}")