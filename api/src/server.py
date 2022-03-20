from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    'http://localhost:5000',
    'http://localhost:3000',
    'http://localhost:80',
    'http://localhost'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

async def dictionary_dependency(value: str) -> dict[str, str]:
    return {"value": value}

class ClassDependency:
    def __init__(self, value: str):
        self.value = value

@app.get('/')
async def hello(
    request: Request,
    class_dep: ClassDependency = Depends(ClassDependency),
    dict_dep: dict[str, str] = Depends(dictionary_dependency),
) -> Response:
    '''
    These dependencies inject query parameters into the API route.
    '''
    v1 = class_dep.value
    v2 = dict_dep['value']
    print(v1,v2)
    return 'Hello World!'