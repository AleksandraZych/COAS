from fastapi import APIRouter

router = APIRouter(prefix="/tenants_crud")


@router.get("/")
def root():
    return {"tenants_crud_response": "in progress"}
