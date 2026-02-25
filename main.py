from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Blog_post_agent import blog_agent
import uvicorn
import os

app = FastAPI()

# Allow CORS for local React dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Blog Writer API is running"}

@app.post("/generate-blog")
async def generate_blog(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    if not topic:
        return JSONResponse({"error": "No topic provided."}, status_code=400)

    def blog_stream():
        try:
            for chunk in blog_agent.run(topic, stream=True):
                if chunk.content is not None:
                    yield chunk.content.encode("utf-8")  # Ensure proper encoding
                else:
                    yield "[INFO].".encode("utf-8")
        except Exception as e:
            print(f"Error in blog_stream: {e}")
            yield f"\n\n[ERROR] {str(e)}".encode("utf-8")  # Encode error message

    return StreamingResponse(blog_stream(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
