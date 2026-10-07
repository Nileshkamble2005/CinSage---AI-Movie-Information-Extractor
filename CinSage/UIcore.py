import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )


model = get_model()

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract movie information from the paragraph.

        {format_instructions}
        """
    ),
    (
        "human",
        "{paragraph}"
    )
])


st.set_page_config(
    page_title="🎬 Movie Info Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")

st.write(
    "Paste any movie description and AI will convert it into structured data."
)


paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=200,
    placeholder="Example: 3 Idiots is a 2009 Hindi comedy-drama film..."
)


if st.button("Extract Data"):

    if not paragraph.strip():

        st.warning("Please enter a paragraph first.")

    else:

        with st.spinner("Analyzing movie..."):

            try:

                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions":
                        parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                st.subheader("Raw Model Output")

                st.code(
                    response.content,
                    language="json"
                )

                movie_data = parser.parse(response.content)

                st.subheader("Structured Output")

                st.json(movie_data.model_dump())

                st.success(
                    "Extraction Completed Successfully!"
                )

            except Exception as e:

                st.error(
                    "Failed to parse response. "
                    "Model did not follow schema."
                )

                st.exception(e)