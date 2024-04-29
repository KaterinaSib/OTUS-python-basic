from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)


@router.get("")
def hello_user(name: str, age: int):
    return {"message": f"Hello {name} of age {age}!"}
