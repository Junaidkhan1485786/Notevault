from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn
import templates
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime



app = FastAPI()

# database se connection setup
MONGO_URI = "mongodb+srv://junaidkhan66094:oCXXYk9XtyR8E6ZM@junaidfirstcluster.yljni.mongodb.net/NotesAPP?retryWrites=true&w=majority"
DATABASE_NAME = "NotesAPP"

# mongodb client or database initilize
client = MongoClient(MONGO_URI)
db = client["NotesAPP"]


# Setting up the templates folder
templates = Jinja2Templates(directory="templates")
# index.html or main app connection 📱📱📱📱📱📱📱📱
@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
# query to check total collections 🪣🪣🪣🪣🪣🪣🪣🪣🪣🪣
@app.get("/database")
async def get_total_collections():
    # List all collections and return the total count
    collections = db.list_collection_names()
    total_collections = len(collections)
    return {"total_collections": total_collections}
# query to check total document inside collection 🪣🪣🪣🪣🪣🪣🪣🪣
@app.get("/get-collection-data/{collection_name}")
async def get_collection_data(collection_name: str):
    # Get the collection data
    collection = db[collection_name]
    documents = list(collection.find({}))  # Fetch all documents

    # Convert documents to list of dictionaries to return as JSON
    data = []
    for doc in documents:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string for JSON serialization
        data.append(doc)

    return {"documents": data}
# फॉर्म डेटा को MongoDB में स्टोर करने के लिए एक POST रूट जोड़ेंगे
@app.post("/submit")
async def submit_note(
        request: Request,
        note_title: str = Form(...), # three dot jiske sath h mtlab wo filed required h , mtlab yha nota title required h
        note_date: str = Form(...),
        note_description: str = Form(...)
):
    try:
        # डेटा को डेटाबेस में इंसर्ट करें
        note_collection = db["note_details"]
        note_data = {
            "title": note_title,
            "date": note_date,
            "description": note_description,
            "created_at": datetime.utcnow()
        }
        note_collection.insert_one(note_data)

        # सफल इंसर्शन के बाद होमपेज पर रीडायरेक्ट करें
        return RedirectResponse(url="/success", status_code=303)
    except Exception as e:
        # एरर हैंडलिंग
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})

# reditrect page
@app.get("/success")
async def success_note():
    return {"message1": "your note added successfully",
            "message2": "you want add more note then change (/success) to (/) endpoint in browser "}
    return RedirectResponse(url="/success", status_code=303)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)
# python -m uvicorn main:app --reload --port 8004

