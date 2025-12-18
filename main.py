from fastapi import FastAPI
from pydantic import BaseModel
from rembg import remove
import base64

app = FastAPI()

class Req(BaseModel):
    base64: str  # raw base64 (no data:image/... prefix)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/remove-bg")
def remove_bg(req: Req):
    img_bytes = base64.b64decode(req.base64)
    out_bytes = remove(img_bytes)  # PNG bytes with alpha
    return {"base64": base64.b64encode(out_bytes).decode("utf-8")}
