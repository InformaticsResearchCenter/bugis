from blacksheep import FromJSON, FromQuery
from model.data import Request, Response
from controller import controller

def site(page):
    url=page.route
    get=page.router.get
    post=page.router.post

    @url("/")
    async def home():
        return controller.home()

    @post("/api")
    async def api(data: FromJSON[Request]):
        return controller.api(data)

    @post("/m/gis/:module_name/:module_func")
    async def gis(module_name, module_func,param: FromJSON[Gis]):
        return controller.gis(module_name,module_func,param)
