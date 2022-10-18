from fastapi import FastAPI
import pokemon_route
import uvicorn

app = FastAPI()
app.include_router(pokemon_route.router)

@app.get("/")
def root():
    return "Server On"

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

