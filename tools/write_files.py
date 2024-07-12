import os
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import List

class WriteJokesInput(BaseModel):
    tv_show: str = Field(..., description="The name of the TV show the jokes are based on")
    jokes: List[str] = Field(..., description="A list of jokes to write to the file")
    file_path: str = Field(..., description="The path where the markdown file should be saved")

class WriteJokesToMarkdownFile(BaseTool):
    name = "write_jokes_to_markdown_file"
    description = "Write jokes inspired by a TV show to a markdown file"
    args_schema = WriteJokesInput

    def _run(self, tv_show: str, jokes: List[str], file_path: str) -> str:
        try:
            # Ensure the input is correct
            if isinstance(tv_show, dict):
                tv_show = tv_show.get('tv_show', '')
                jokes = tv_show.get('jokes', [])
                file_path = tv_show.get('file_path', '')
             # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# Jokes Inspired by {tv_show}\n\n")
                for i, joke in enumerate(jokes, 1):
                    f.write(f"## Joke {i}\n")
                    f.write(f"{joke}\n\n")
            return f"Jokes successfully written to {file_path}"
        except Exception as e:
            return f"Error writing jokes to file: {str(e)}"

    async def _arun(self, tv_show: str, jokes: List[str], file_path: str) -> str:
        # This is the asynchronous version of the run method.
        # For this tool, we can just call the synchronous version.
        return self._run(tv_show, jokes, file_path)

class WriteFiles:
    write_jokes_to_markdown_file = WriteJokesToMarkdownFile()