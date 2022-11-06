from blacksheep import FromJSON, FromQuery
from model.data import Request, Response

def site(page):
    @page.route("/")
    async def home():
        anu='croot'
        return f"Hello, World! {anu}"


    @page.router.post("/api")
    async def example(data: FromJSON[Request]):
        # in this example, data is bound automatically reading the JSON
        # payload and creating an instance of `CreateCatInput`
        data.value.message = 'hai nomor ' + data.value.number
        resp = Response
        resp.message=data.value.message
        resp.request=data.value
        return (resp)

    @page.router.get("/:culture_code/:area")
    async def home(culture_code, area):
        # in this example, both parameters are obtained from routes with
        # matching names
        return f"Request for: {culture_code} {area}"


    @page.router.get("/api/products")
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


    @page.router.get("/api/products2")
    def get_products2(
        page: FromQuery[int] = FromQuery(1),
        size: FromQuery[int] = FromQuery(30),
        search: FromQuery[str] = FromQuery(""),
    ):
        # this example illustrates support for explicit query parameters with
        # default values
        # in this case, parameters are explicitly read from query string
        ...