import nltk
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('punkt')

def read_terms(file_path):
    """
    Reads terms and conditions from a given file path.

    :param file_path: Path to the terms and conditions file.
    :return: Content of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            terms = file.read()
        return terms
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def evaluate_terms(terms):
    """
    Evaluates the safety of the terms and conditions using a simple keyword-based approach.

    :param terms: String containing the terms and conditions.
    :return: Evaluation result based on keyword analysis.
    """
    if terms is None:
        return None
    
    # Define keywords that might indicate unsafe terms
    unsafe_keywords = [
        "waive", "liability", "dispute", "binding", "arbitration", "third-party",
        "tracking", "data collection", "no refund", "no liability", "disclaimer",
        "indemnify", "automatic renewal", "termination"
    ]
    
    # Tokenize the terms and conditions
    words = nltk.word_tokenize(terms.lower())
    
    # Count occurrences of unsafe keywords
    keyword_counts = Counter(word for word in words if word in unsafe_keywords)
    
    total_keywords = sum(keyword_counts.values())
    safe_count = len(words) - total_keywords
    
    return {
        'safe': safe_count,
        'not_safe': total_keywords,
        'keyword_counts': keyword_counts
    }

def visualize_evaluation(evaluation):
    """
    Visualizes the evaluation of the terms and conditions using a pie chart.

    :param evaluation: The evaluation result from the keyword analysis.
    """
    if evaluation is None:
        print("No evaluation to visualize.")
        return

    labels = ['Safe', 'Not Safe']
    sizes = [evaluation['safe'], evaluation['not_safe']]
    colors = ['#4CAF50', '#FF0000']
    explode = (0.1, 0)  # explode the 'Safe' slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Terms and Conditions Safety Evaluation')
    plt.show()

def main(file_path):
    """
    Main function to read, evaluate, and visualize the terms and conditions.

    :param file_path: Path to the terms and conditions file.
    """
    terms = read_terms(file_path)
    if terms:
        evaluation = evaluate_terms(terms)
        visualize_evaluation(evaluation)

if __name__ == "__main__":
    # Example usage
    terms_file_path = 'terms.txt'  # Update with your file path
    main(terms_file_path)