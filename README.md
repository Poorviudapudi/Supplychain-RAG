
# Supply Chain Documents RAG System
<img width="1280" height="720" alt="WhatsApp Image 2026-08-14 at 5 15 26 PM" src="https://github.com/user-attachments/assets/2d8a806f-47f4-4ebb-bd19-80aac7c49162" />
<img width="1600" height="900" alt="WhatsApp Image 2026-08-14 at 5 15 25 PM" src="https://github.com/user-attachments/assets/d90e6861-2985-42af-acf4-ac1d7497141f" />
<img width="1280" height="720" alt="WhatsApp Image 2026-08-14 at 5 15 25 PM (1)" src="https://github.com/user-attachments/assets/a8d0bc52-9e70-4248-bf7f-cab635f3b8be" />
<img width="1600" height="900" alt="WhatsApp Image 2026-08-14 at 5 15 25 PM" src="https://github.com/user-attachments/assets/37a7df88-43d9-4619-aeaa-80732ec1beb8" />
<img width="1280" height="720" alt="WhatsApp Image 2026-08-14 at 5 15 25 PM (1)" src="https://github.com/user-attachments/assets/0c191ba8-0203-4b04-8201-e55f95a5b38f" />
<img width="1280" height="720" alt="WhatsApp Image 2026-08-14 at 5 15 26 PM" src="https://github.com/user-attachments/assets/2851fb0c-faad-478e-9889-7a220de1dcc1" />
<img width="1920" height="1080" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/c64f1a3a-25d9-44b6-ab33-8992495e3626" />
<img width="1920" height="1080" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/1acdc001-3da5-46ed-93f5-ac3cb0c26b3c" />
<img width="1920" height="1080" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/d27b4916-ea8d-424e-b32c-27b55bf29f77" />
<img width="1920" height="1080" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/12c0ccf7-96c6-42da-b12f-03eb1ece852e" />
<img width="1920" height="1080" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/ad5be366-822a-4d24-a771-46d90df98ba5" />
<img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/2410faae-1fe4-4f2d-ba5f-261d9d8cd606" />
<img width="1920" height="1080" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/76136c5f-35d1-4416-aa10-5469a3fa4b2b" />

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

## Test Questions

*(Run the app, ask these questions, and paste the results below to complete the assignment)*

1. Which supplier had the highest spend in Q1, and what was its on-time delivery percentage?
   > Answer: Shenzhen Rui Electronics had the highest spend in Q1 at ₹21.9 crore, and its on-time delivery percentage was 79.5%

2. How many line stoppages happened in Q1, what was the total downtime, and what caused them?
   > Answer: According to the context, the following line stoppages happened in Q1 (April to June, but only April is in Q1, and the rest are in Q2):

In Q1 (April), there was 1 line stoppage:

Date: 12 Apr 2025
Plant: Chakan
Duration: 4 hours
Root cause: Microcontroller shortage — vessel roll-over at Shenzhen
The total downtime in Q1 was 4 hours.

3. What is the approval authority for a purchase order worth ₹1.4 crore?
   > Answer: The approval authority for a purchase order worth ₹1.4 crore is the Chief Operating Officer. According to the context, the approval authority for purchase orders above ₹1 crore and up to ₹5 crore is the Chief Operating Officer.

4. What are the four supplier classification categories, and what qualifies a supplier as Critical?
   > Answer: The four supplier classification categories are:

Critical
Strategic
Standard
Tail
A supplier is qualified as Critical if it meets any of the following criteria:

Single-source for any part
Annual spend above ₹10 crore
Supplies a safety-related component.

5. Kaveri Metals recorded 88.1% on-time delivery and 1,150 defects per million in Q1. Which policy clauses does this trigger, and what exactly must the buyer do?
   > Answer: The information provided about Kaveri Metals' performance in Q1 (88.1% on-time delivery and 1,150 defects per million) does not match the context provided, as the context only mentions Kaveri Metals' issue with burr formation on stamped contacts during May 2025, but does not provide the specific on-time delivery percentage or defect rate for Q1.

However, based on the policy clauses provided:

The on-time delivery of 88.1% is above 85%, so it does not trigger clause 6.1 or 6.2.
The defect rate of 1,150 defects per million is above 500 parts per million, which triggers clause 6.3.
According to clause 6.3, the supplier (Kaveri Metals) bears the cost of rework at a standard recovery rate of ₹120 per affected unit, and 100% incoming inspection is imposed at the supplier's cost until three consecutive lots are accepted without defect.

The information about what the buyer must do in this specific situation is not available in the uploaded documents, but according to clause 6.3, the buyer must impose 100% incoming inspection at the supplier's cost.

6. The microcontroller supplier is single-source. What does the sourcing policy require in this situation, and what is the company already doing about it?
   > Answer: The information provided does not explicitly state the sourcing policy requirements in the situation of a single-source supplier. However, it is mentioned that the single largest structural risk carried into Q2 is the absence of a second source for microcontrollers, and qualification of an alternate supplier is under way (discussed in Section 8). Additionally, there is an action item to "Shift 30% of Shenzhen microcontroller volume to air freight on a planned basis until dual sourcing is live" which indicates that the company is taking steps to mitigate the risk of single sourcing.

7. Microcontrollers are imported with a 46-day lead time. Using the safety-stock policy, how many days of stock should be held for this part?
   > Answer: To calculate the safety stock, we need to use the formula: Safety stock (days) = lead time in days × 0.25.

Given the lead time is 46 days, the calculated safety stock would be: Safety stock (days) = 46 × 0.25 = 11.5 days.

However, according to the safety stock policy, the minimum safety stock for imported parts (not supplied by a Critical supplier) is 10 days. Since 11.5 days is higher than the minimum floor of 10 days, the higher value applies.

So, the safety stock for microcontrollers should be 11.5 days, but since the policy does not specify fractional days, it is likely rounded. However, based on the provided information, the exact rounding rule is not available.

8. Trident Circuit Boards had a defect rate of 640 parts per million. What is the cost consequence under the policy?
   > Answer: The information about the cost consequence specific to Trident Circuit Boards' defect rate is not available in the uploaded documents. However, the total cost of poor quality attributable to incoming material is ₹0.74 crore, comprising rework of ₹0.41 crore, sorting and containment of ₹0.19 crore, and scrap of ₹0.14 crore.

9. Which suppliers would fall below the B rating band on on-time delivery alone, and what is the escalation path for them?
   > Answer: According to the context, suppliers delivering below 75% on-time delivery cannot score in band B.

The escalation path for suppliers with on-time delivery below 90% in any quarter is:

A written warning is issued to the supplier within 10 working days of quarter close, and
The supplier moves to a weekly delivery review call until performance recovers above 90% for one full quarter (as per clause 6.1).
Additionally, if the on-time delivery is below 85% for two consecutive quarters, a debit note is issued in addition to the above actions (as per clause 6.2).

10. What is the annual salary of the Head of Procurement? (Trap Question)
    > Answer: The information is not available in the uploaded documents. The context only mentions the role and responsibilities of the Head of Procurement, but does not provide any information about their annual salary.
