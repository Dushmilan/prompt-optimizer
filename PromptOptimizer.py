import google.generativeai as ai
import argparse
import sys

class PromptOptimizer:
    """
    Class to optimize a prompt using Google's Generative AI.

    Attributes:
            prompt (str): The prompt to optimize
            api_key (str): Google Generative AI API key
        """

    def __init__(self, prompt: str, api_key: str = None):
        """Initialize the PromptOptimizer

        Args:
            prompt (str): The prompt to optimize
            api_key (str, optional): Google Generative AI API key
                            """
        self.prompt = prompt
        self.api_key = api_key
        if api_key:
            ai.configure(api_key=api_key)

    def get_model(self):
        """Initializes and returns the generative model

        Returns:
            ai.GenerativeModel: The configured generative model
        """
        return ai.GenerativeModel('gemini-2.5-flash')

    def optimize(self, iterations: int) -> str:
        """Optimize the prompt through multiple iterations

        Args:
            iterations (int): Number of optimization iterations

        Returns:
            str: The optimized prompt

        Raises:
            ValueError: If iterations is not a positive integer
        """
        if iterations <= 0:
            raise ValueError("Iterations must be a positive integer")

        current_prompt = self.prompt
        model_instance = self.get_model()

        for i in range(iterations):
            optimization_prompt = f"""
                            You are an expert **Prompt Refinement and Standardization Engine**. Your goal is to rewrite the user's 'Original Prompt' to conform to best-in-class prompt engineering standards for a Large Language Model (LLM).

                            Your revision must implement the following **mandatory best practices**:

                            1.  **Assign a Clear Role:** Start the prompt by giving the model an authoritative, specific persona (e.g., "You are a professional copywriter," or "You are a meticulous JSON formatter").
                            2.  **Explicit Constraints:** Add clear, specific rules that the LLM must follow (e.g., "NEVER hallucinate," "Limit the response to 3 sentences," "Do not include any conversational preamble").
                            3.  **Structured Output Request (if applicable):** If the prompt implies a structured output (like a list, table, or JSON), explicitly request that structure and define its fields/format.
                            4.  **Clarity & Brevity:** Refactor vague language into explicit, simple commands. Remove any unnecessary fluff or redundancy.
                            5.  **Place Variable Content Last:** Ensure the original prompt's core instructions are defined first, and any placeholder for user input or variable content is clearly indicated at the end (e.g., "The text to summarize is: [INPUT_TEXT]").

                            ---
                            **Original Prompt to be optimized:**
                            {current_prompt}

                            ---
                            **OUTPUT REQUIREMENT:**
                            Provide **ONLY** the full, single, optimized prompt string as your entire response. Do not include any headers, commentary, or markdown code fences (```). The output must be ready to be used as a new prompt template.
                            """
            try:
                response = model_instance.generate_content(optimization_prompt)
                if not response.text:
                    print(f"Warning: Empty response in iteration {i+1}")
                    break
                current_prompt = response.text.strip()
                print(f"Iteration {i+1}: {current_prompt}")
            except Exception as e:
                        print(f"Error in iteration {i+1}: {e}")
                        break
        return current_prompt

def main():
    parser = argparse.ArgumentParser(description='Optimize prompts using AI')
    parser.add_argument("prompt", help="The prompt to optimize")
    parser.add_argument("-i", "--iterations", type=int, default=1,
                       help="Number of optimization iterations")
    parser.add_argument("-k", "--api-key", required=True,
                       help="Google Generative AI API key")

    try:
        args = parser.parse_args()
        optimizer = PromptOptimizer(args.prompt, args.api_key)
        optimized_prompt = optimizer.optimize(args.iterations)
        print("\nFinal Optimized Prompt:")
        print("=" * 50)
        print(optimized_prompt)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)  # Fixed typo: strderr -> stderr
        sys.exit(1)

if __name__ == "__main__":
    main()


