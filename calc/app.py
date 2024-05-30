# Put your app in here.
#further study was confusing because it was giving me failures as it expects both versions of code with and without /math
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/math/<operation>')
def math_operation(operation):
    # Get the 'a' and 'b' parameters from the request
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Perform the appropriate operation based on the URL
    if operation == 'add':
        result = add(a, b)
    elif operation == 'sub':
        result = sub(a, b)
    elif operation == 'mult':
        result = mult(a, b)
    elif operation == 'div':
        result = div(a, b)
    else:
        # If the operation is not supported, return an error message
        return 'Unsupported operation', 400

    # Return the result as a string
    return str(result)


#original
# @app.route('/add')
# def addition():
#     #get the args from request and use them in function from operations
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = add(a,b)
#     return str(result)

# @app.route('/sub')
# def subtraction():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = sub(a,b)
#     return str(result)

# @app.route('/mult')
# def multiply():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = mult(a,b)
#     return str(result)

# @app.route('/div')
# def division():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = div(a,b)
#     return str(result)
    
