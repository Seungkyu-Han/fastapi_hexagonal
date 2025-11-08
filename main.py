from fastapi import FastAPI
from users import user_router


app = FastAPI(title='JWT 인증서비스 헥사고날 아키텍처로 구현')

app.include_router(user_router)