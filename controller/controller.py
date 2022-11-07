def home():
    anu='croot'
    return f"Hello, World! {anu}"

def api(data):
    data.value.message = 'hai nomor ' + data.value.number
    return (data.value)

def gis(country_code,module_name,module_func,param):
    m=__import__('module.gis.'+country_code+'.'+module_name, globals(), locals(), [module_name])
    return getattr(m,module_func)(param)
