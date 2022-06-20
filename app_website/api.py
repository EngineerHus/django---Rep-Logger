from ninja import NinjaAPI


api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    a = 5
    b = 7
    return {"result": a + b}





