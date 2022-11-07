def home():
    anu='croot'
    return f"Hello, World! {anu}"

def api(data):
    data.value.message = 'hai nomor ' + data.value.number
    return (data.value)

def gis(module_name,module_func,param):
    m=__import__('module.gis.SG.'+module_name, globals(), locals(), [module_name])
    res=getattr(m,module_func)(param)
    return f"Request for: module {module_name} with function {module_func} has param {param.value}"