from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}={q}")
def read_item(item_id: int, q: str | None = None):
    if item_id > 1:
      return{""""
                Kahan bechna sahi rahega:

                     Samsung Assured Buyback: agar aapne ye plan liya tha, to 12 mahine ke andar bechne par phone ki resale value ka 70% milta hai. Bill check kar lo. 
                    sammobile
                    Cashify / Amazon ya Flipkart exchange: jaldi aur safe hai,"""}
    else:
        return{"""HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HTTP/1.1" 200 OK
                INFO:     127.0.0.1:54970 - "GET /items/6%3D1 HT"""}