import time
import os
from evaluator import read_terms, evaluate_terms
from visualizer import visualize_evaluation
from notifier import send_notification

TERMS_FILE_PATH = 'terms.txt'

def monitor_terms_file(file_path):
    last_modified_time = os.path.getmtime(file_path)
    while True:
        current_modified_time = os.path.getmtime(file_path)
        if current_modified_time != last_modified_time:
            last_modified_time = current_modified_time
            terms = read_terms(file_path)
            evaluation = evaluate_terms(terms)
            summary = f"Safe: {evaluation['safe']}, Not Safe: {evaluation['not_safe']}"
            send_notification("Terms Evaluation Result", summary)
            visualize_evaluation(evaluation)
        time.sleep(10)

if __name__ == "__main__":
    monitor_terms_file(TERMS_FILE_PATH)