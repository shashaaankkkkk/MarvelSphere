import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



genai.configure(api_key="AIzaSyCnhDeX2uEy-qFRohEJLpYVrl75kvuSK80")
model = genai.GenerativeModel('gemini-pro')