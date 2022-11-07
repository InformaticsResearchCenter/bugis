from blacksheep import Application
from url import web

page = Application()
page.serve_files("static/img")
web.site(page)
