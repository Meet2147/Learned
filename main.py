from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from datetime import date

app = FastAPI()

feedback_data = []

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <head>
            <title>Lecturer Feedback App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                }
                label {
                    font-weight: bold;
                }
                input[type="text"],
                input[type="date"],
                select {
                    width: 100%;
                    padding: 10px;
                    margin: 5px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    box-sizing: border-box;
                }
                select {
                    appearance: none;
                }
                input[type="submit"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0 0;
                    border: none;
                    border-radius: 5px;
                    background-color: #4CAF50;
                    color: white;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Lecturer Feedback App</h1>
                <p>Please provide your feedback below:</p>
                <form method="post">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required><br>
                    <label for="date">Date:</label>
                    <input type="date" id="date" name="date" required><br><br>
                    <label for="clarity">Clarity of Explanation:</label>
                    <select id="clarity" name="clarity" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br>
                    <label for="engagement">Engagement:</label>
                    <select id="engagement" name="engagement" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br>
                    <label for="knowledge">Knowledge:</label>
                    <select id="knowledge" name="knowledge" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br>
                    <label for="preparedness">Preparedness:</label>
                    <select id="preparedness" name="preparedness" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br>
                    <label for="communication">Communication:</label>
                    <select id="communication" name="communication" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br>
                    <label for="satisfaction">Overall Satisfaction:</label>
                    <select id="satisfaction" name="satisfaction" required>
                        <option value="1">*</option>
                        <option value="2">**</option>
                        <option value="3">***</option>
                        <option value="4">****</option>
                        <option value="5">*****</option>
                    </select><br><br>
                    <label for="feedback_notes">Feedback Notes:</label>
                    <input type="text" id="feedback_notes" name="feedback_notes"><br><br>
                    <input type="submit" value="Submit Feedback">
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/")
async def submit_feedback(name: str = Form(...), date: date = Form(...),
                          clarity: int = Form(...), engagement: int = Form(...), knowledge: int = Form(...),
                          preparedness: int = Form(...), communication: int = Form(...),
                          satisfaction: int = Form(...), feedback_notes:str = Form(...)):

    feedback_data.append({
        "Name": name,
        "Date": date,
        "Clarity of Explanation": clarity,
        "Engagement": engagement,
        "Knowledge": knowledge,
        "Preparedness": preparedness,
        "Communication": communication,
        "Overall Satisfaction": satisfaction,
        "Notes": feedback_notes
    })

    return {"message": "Feedback submitted successfully!"}

@app.get("/feedback", response_model=list)
async def get_feedback():
    return feedback_data
