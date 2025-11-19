from app import create_app

app = create_app()

@app.get("/")
def home():
    return {"message": "OCR service is running"}

if __name__ == "__main__":
    app.run(port=8001, host="0.0.0.0")
