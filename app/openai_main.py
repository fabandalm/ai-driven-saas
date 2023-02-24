import os
import openai
import argparse


def main():
    print("openai_main!")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    generate_branding(user_input)
    pass


def generate_branding(prompt: str):
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_prompt = f"Generate upbeat branding snippet for {prompt}"

    response = openai.Completion.create(engine="davinci-instruct-beta", prompt=enriched_prompt,
                                        max_tokens=32)

    print(response)
    text = response["choices"][0]["text"]
    print(text)


if __name__ == "__main__":
    main()


