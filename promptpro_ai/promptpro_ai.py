import openai

class PromptProAI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_test_scenario(self, feature_description):
        prompt = f"""
        Create a BDD test scenario for the following feature:
        {feature_description}
        
        Use the format:
        Given...
        When...
        Then...
        """
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200
        )
        
        return response.choices[0].text.strip()

    def convert_to_gherkin(self, scenario):
        # Implementação futura para converter cenários para formato Gherkin
        pass

# Exemplo de uso
if __name__ == "__main__":
    api_key = "your_openai_api_key_here"
    promptpro = PromptProAI(api_key)
    
    feature = "A user should be able to log in to the system using email and password"
    scenario = promptpro.generate_test_scenario(feature)
    print(scenario)
