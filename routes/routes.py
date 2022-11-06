from blacksheep import FromJSON, FromQuery
from model.request import IteungInput

def routes(app):
    @app.route("/")
    async def home():
        anu='croot'
        return f"Hello, World! {anu}"


    @app.router.post("/api")
    async def example(data: FromJSON[IteungInput]):
        # in this example, data is bound automatically reading the JSON
        # payload and creating an instance of `CreateCatInput`
        data.value.message = 'hai nomor ' + data.value.number
        return (data.value)

    @app.router.get("/:culture_code/:area")
    async def home(culture_code, area):
        # in this example, both parameters are obtained from routes with
        # matching names
        return f"Request for: {culture_code} {area}"


    @app.router.get("/api/products")
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


    @app.router.get("/api/products2")
    def get_products2(
        page: FromQuery[int] = FromQuery(1),
        size: FromQuery[int] = FromQuery(30),
        search: FromQuery[str] = FromQuery(""),
    ):
        # this example illustrates support for explicit query parameters with
        # default values
        # in this case, parameters are explicitly read from query string
        ...