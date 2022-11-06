def home():
    anu='croot'
    return f"Hello, World! {anu}"

def api(data):
    data.value.message = 'hai nomor ' + data.value.number
    return (data.value)