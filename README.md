# 🎬 CinSage — AI Movie Information Extractor

**CinSage** is an AI-powered movie information extraction application that converts unstructured movie descriptions into structured movie data using **Google Gemini, LangChain, Pydantic, and Streamlit**.

Simply enter a movie description, and CinSage extracts important information such as the **movie title, release year, genre, director, cast, rating, and summary**.

---

## 🚀 Features

- 🎬 Extract movie title
- 📅 Extract release year
- 🎭 Identify movie genre
- 🎥 Extract director
- 👥 Extract cast members
- ⭐ Extract movie rating
- 📝 Extract movie summary
- 🤖 Google Gemini 2.5 Flash integration
- 🔗 LangChain integration
- 📋 Pydantic structured output
- 🖥️ Interactive Streamlit interface
- ⚡ Fast AI-powered information extraction

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🤖 Google Gemini 2.5 Flash | AI / LLM |
| 🔗 LangChain | LLM Application Framework |
| 📋 Pydantic | Data Validation & Structured Output |
| 🎨 Streamlit | Web Interface |
| 🔐 python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
CinSage/
│
├── CinSage/
│   ├── core.py          # Core AI and movie extraction logic
│   └── UIcore.py       # Streamlit user interface
│
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies
```

---

## 🏗️ Architecture

```text
                👤 User
                  │
                  ▼
        ┌──────────────────┐
        │   Streamlit UI   │
        │    UIcore.py     │
        └────────┬─────────┘
                 │
                 ▼
        Movie Description
                 │
                 ▼
        ┌──────────────────┐
        │     core.py      │
        │                  │
        │ LangChain Prompt │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Google Gemini    │
        │   2.5 Flash      │
        └────────┬─────────┘
                 │
                 ▼
        AI Generated Output
                 │
                 ▼
        ┌──────────────────┐
        │ Pydantic Parser  │
        └────────┬─────────┘
                 │
                 ▼
        Structured Movie Data
                 │
                 ▼
        🎬 Streamlit Output
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CinSage.git
```

### 2. Navigate to the Project

```bash
cd CinSage
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

CinSage uses the **Google Gemini API**.

Create a `.env` file in the **root CinSage directory**, at the same level as `README.md` and `requirements.txt`:

```text
CinSage/
│
├── CinSage/
│   ├── core.py
│   └── UIcore.py
│
├── .env
├── README.md
└── requirements.txt
```

Add your Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ **Important:** Never upload your `.env` file or API key to GitHub.

Add `.env` to your `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

## ▶️ Run the Application

From the **root CinSage directory**, run:

```bash
streamlit run CinSage/UIcore.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 💡 How CinSage Works

### 1. Enter Movie Description

The user enters an unstructured movie description.

Example:

```text
3 Idiots is a 2009 Hindi comedy-drama film directed by Rajkumar Hirani.
It stars Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor and
Boman Irani. The movie is about three engineering students and their
college life. It has a rating of 8.4.
```

### 2. Prompt Processing

The movie description is passed to the LangChain prompt along with the required output format.

### 3. Gemini Processing

**Google Gemini 2.5 Flash** analyzes the movie description and extracts the required information.

### 4. Structured Output

The response is processed using **PydanticOutputParser** to ensure the output follows the predefined movie schema.

### 5. Display

The extracted information is displayed in the Streamlit application as structured data.

---

## 📊 Example Output

```json
{
    "title": "3 Idiots",
    "release_year": 2009,
    "genre": [
        "Comedy",
        "Drama"
    ],
    "director": "Rajkumar Hirani",
    "cast": [
        "Aamir Khan",
        "R. Madhavan",
        "Sharman Joshi",
        "Kareena Kapoor",
        "Boman Irani"
    ],
    "rating": 8.4,
    "summary": "The movie follows three engineering students and their college life."
}
```

---

## 🧠 Movie Data Schema

CinSage uses a Pydantic model to define the expected output:

```python
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str
```

This provides a consistent structure for the information extracted by the LLM.

---

## 📁 File Description

### `CinSage/core.py`

Contains the main AI processing logic:

- Google Gemini model
- Movie Pydantic schema
- LangChain prompt
- Pydantic output parser
- Movie information extraction

### `CinSage/UIcore.py`

Contains the Streamlit application:

- User input
- Extract Data button
- Loading state
- AI response
- Structured output
- Error handling

### `requirements.txt`

Contains the Python packages required to run CinSage.

### `README.md`

Contains project documentation, installation instructions, architecture, and usage information.

---

## 🎯 Learning Outcomes

Building CinSage helped me gain practical experience in:

- 🤖 Generative AI
- 🧠 Large Language Models
- 🔗 LangChain
- ✨ Google Gemini
- 📝 Prompt Engineering
- 📋 Pydantic
- 📊 Structured Data Extraction
- 🐍 Python
- 🎨 Streamlit
- 🔐 Environment Variables
- 🚀 AI Application Development

---

## 🔮 Future Enhancements

- 🎞️ Movie poster integration
- 🔍 Movie API/database integration
- 🌐 Multilingual movie extraction
- 🎤 Voice-based input
- 🤖 AI movie recommendation system
- 💾 Database storage
- 🔎 Movie search and filtering
- ☁️ Cloud deployment
- 📱 Responsive UI improvements

---

## 🎥 Project Demo

A demonstration video showcasing the CinSage application is available on my LinkedIn profile.

The demo shows:

1. Entering a movie description
2. Sending the description to Gemini
3. AI-powered information extraction
4. Structured Pydantic output
5. Displaying the final movie information

---

## 👨‍💻 Author

**Nilesh Kamble**

**B.Tech — Artificial Intelligence & Data Science**

### Areas of Interest

- Artificial Intelligence
- Data Science
- Machine Learning
- Computer Vision
- Generative AI

---

## ⭐ Support

If you found **CinSage** useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational and learning purposes.
