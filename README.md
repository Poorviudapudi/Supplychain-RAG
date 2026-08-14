
# Supply Chain Documents RAG System

This project is a Retrieval-Augmented Generation (RAG) system for Supply Chain Documents, satisfying all assignment requirements.

## Setup Instructions

1. **Clone the repository** (if not already downloaded)
   ```bash
   cd supplychain-rag
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**
   - Copy `.env.example` to a new file named `.env`
   - Add your API key inside `.env`: `OPENAI_API_KEY=your_openai_api_key_here`

4. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```
   You can then upload the generated PDFs and test the system.

5. **(Optional) Run the FastAPI backend**
   ```bash
   uvicorn api.main:app --reload
   ```
   Access the API docs at `http://localhost:8000/docs` to test endpoints like `/ingest`, `/ask`, and `/stats`.

## Chunking Strategy
- **Chunk Size:** 1000 characters
- **Chunk Overlap:** 150 characters
- **Reason:** A chunk size around 1000-1200 keeps full tables together and improves answers considerably, preventing information fragmentation while keeping context windows efficient for the embedding model.

## Screenshots
*(Add screenshots of the working Streamlit App here)*

## Test Questions

*(Run the app, ask these questions, and paste the results below to complete the assignment)*

1. Which supplier had the highest spend in Q1, and what was its on-time delivery percentage?
   > Answer: 

2. How many line stoppages happened in Q1, what was the total downtime, and what caused them?
   > Answer: 

3. What is the approval authority for a purchase order worth ₹1.4 crore?
   > Answer: 

4. What are the four supplier classification categories, and what qualifies a supplier as Critical?
   > Answer: 

5. Kaveri Metals recorded 88.1% on-time delivery and 1,150 defects per million in Q1. Which policy clauses does this trigger, and what exactly must the buyer do?
   > Answer: 

6. The microcontroller supplier is single-source. What does the sourcing policy require in this situation, and what is the company already doing about it?
   > Answer: 

7. Microcontrollers are imported with a 46-day lead time. Using the safety-stock policy, how many days of stock should be held for this part?
   > Answer: 

8. Trident Circuit Boards had a defect rate of 640 parts per million. What is the cost consequence under the policy?
   > Answer: 

9. Which suppliers would fall below the B rating band on on-time delivery alone, and what is the escalation path for them?
   > Answer: 

10. What is the annual salary of the Head of Procurement? (Trap Question)
    > Answer: 
