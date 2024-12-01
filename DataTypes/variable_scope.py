global_var = "I'm global"

def modify_global():
    global global_var
    global_var = "Modified global variable"

modify_global()
print(global_var)  # Output: Modified global variable
