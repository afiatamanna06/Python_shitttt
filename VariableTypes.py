def function():
    global x
    print(x)
    x = 'local'
    print(x)


x = 'global'
function()
print(x)
