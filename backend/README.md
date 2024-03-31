# Backend

1. To install the openAI python library, `pip install --upgrade openai`
2. Open zshrc using `nano ~/.zshrc` (for older MacOS versions, do `nano ~/.bash_profile`), and add `export OPEN_API_KEY=...` at then end and save changes
- When running imported functions using tokenizer, must also set `export TOKENIZERS_PARALLELISM=true`

## Alternatively for step 2,
- Create a `.env` file with the single line `OPENAI_API_KEY=...`
- In the terminal in the backend folder, run `export OPEN_API_KEY=...` 