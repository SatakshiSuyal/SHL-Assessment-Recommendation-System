
# 📊 SHL Assessment Recommender

An intelligent web application that recommends the best SHL assessments tailored to your hiring needs using semantic search, filters, and AI-powered logic.

---

## 🧠 Overview

The **SHL Assessment Recommender** helps recruiters and HR teams discover the most relevant SHL assessments. It uses semantic similarity to understand your query and return top-matching assessments based on content, category, and duration.

Built using:
- 🧠 Sentence Transformers (`all-MiniLM-L6-v2`)
- ⚙️ Streamlit for UI
- 🤖 Data scraped using Deepseek AI
- 📁 JSON file for structured storage

---

## ✨ Features

- 🔍 **Semantic Search**: Enter your hiring needs in natural language.
- 🗂️ **Category Filtering**: Choose specific assessment categories.
- ⏱️ **Duration Control**: Set a max duration in minutes.
- 📄 **Detailed Results**: See full assessment details, skills tested, and links.
- 🚀 **Deployable on Hugging Face Spaces**

---

## 🏗️ Tech Stack

| Component       | Technology                          |
|----------------|--------------------------------------|
| UI Framework    | Streamlit                           |
| NLP Model       | SentenceTransformers (MiniLM-L6-v2) |
| Core Logic      | Python (OOP-based recommender)      |
| Data Source     | SHL scraped using Deepseek AI       |
| Deployment      | Hugging Face Spaces                 |

---

## 📁 Project Structure

├── main.py                   # Streamlit App Interface
├── recommender_api.py        # Core logic and filtering
├── shl_assessments_complete.json  # Parsed SHL assessment data
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview


🔎 How It Works
- Data Scraping: SHL assessment data is extracted using Deepseek AI and stored in a structured JSON format.

- Embedding Generation: Each assessment’s description is encoded into vector embeddings using Sentence Transformers.

- User Query Processing: A user provides a natural language description of hiring needs.

- Similarity Scoring: The app computes cosine similarity between the query and each assessment.

- Filter Application: Optional filters for category and duration refine the result set.

- Recommendation Display: Top 5 relevant assessments are displayed with expandable details

🚀 Usage :
- Open the app on Hugging Face Spaces.

- Enter a detailed hiring need (e.g., "We need a cognitive test for junior developers").

- Adjust category and duration filters from the sidebar (optional).

- Click Get Recommendations.

- View and explore the suggested assessments.
