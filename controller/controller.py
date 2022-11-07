def home():
    html=```
    <html>
    <head>
    <title>Bugis Framework</title>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    </head>
    <body>

    <h1>Welcome to Bugis Framework</h1>
    <p>Mencari kambing hitam sambil makan bugis</p>

    </body>
    </html>
    ```
    return html

def api(data):
    data.value.message = 'hai nomor ' + data.value.number
    return (data.value)

def gis(country_code,module_name,module_func,param):
    m=__import__('module.gis.'+country_code+'.'+module_name, globals(), locals(), [module_name])
    return getattr(m,module_func)(param)
