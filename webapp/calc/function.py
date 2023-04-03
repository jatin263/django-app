from calc.speechRecog import speechToText


def handle_uploaded_file(f):  
    with open('calc/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks(): 
            destination.write(chunk)
        return speechToText('calc/static/upload/'+f.name)