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

    @get("/m/:culture_code/:area")
    async def culture(culture_code, area):
        # in this example, both parameters are obtained from routes with
        # matching names
        return f"Request for: {culture_code} {area}"

    @get("/:culture_code/:area")
    async def culture(culture_code, area):
        # in this example, both parameters are obtained from routes with
        # matching names
        return f"Request for: {culture_code} {area}"


    @get("/api/products")
    def get_products(
        page: int = 1,
        size: int = 30,
        search: str = "",
    ):
        # this example illustrates support for implicit query parameters with
        # default values
        # since the source of page, size, and search is not specified and no
        # route parameter matches their name, they are obtained from query string
        ...


    @get("/api/products2")
    def get_products2(
        page: FromQuery[int] = FromQuery(1),
        size: FromQuery[int] = FromQuery(30),
        search: FromQuery[str] = FromQuery(""),
    ):
        # this example illustrates support for explicit query parameters with
        # default values
        # in this case, parameters are explicitly read from query string
        ...