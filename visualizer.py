import matplotlib.pyplot as plt

def visualize_evaluation(evaluation):
    labels = ['Safe', 'Not Safe']
    sizes = [evaluation['safe'], evaluation['not_safe']]
    colors = ['#4CAF50', '#FF0000']
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Terms and Conditions Safety Evaluation')
    plt.show()