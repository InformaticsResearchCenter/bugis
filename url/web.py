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

    @post("/m/gis/:culture_code/:area")
    async def gis(culture_code, area,data: FromJSON[Request]):
        # in this example, both parameters are obtained from routes with
        # matching names
        return f"Request for: {culture_code} {area}"
