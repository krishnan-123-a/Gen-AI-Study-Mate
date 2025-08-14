"""
Create a demo PDF for testing automatic quiz generation
"""

import fitz  # PyMuPDF

def create_demo_pdf():
    """Create a sample PDF with machine learning content for quiz testing"""
    
    # Create new PDF
    doc = fitz.open()
    page = doc.new_page()
    
    # Title
    page.insert_text((50, 50), "Machine Learning Fundamentals", fontsize=18, color=(0, 0, 0))
    
    # Content
    content = """
Machine Learning Overview

Machine learning is a subset of artificial intelligence that enables computer systems to automatically learn and improve from experience without being explicitly programmed. It focuses on developing algorithms that can access data and use it to learn patterns.

Types of Machine Learning:

1. Supervised Learning
Supervised learning uses labeled training data to learn a mapping function from input variables to output variables. The algorithm learns from examples where the correct answer is provided.

Examples include:
- Classification: Predicting categories (spam vs. not spam emails)
- Regression: Predicting continuous values (house prices, stock prices)

Common supervised learning algorithms:
- Linear Regression: Used for predicting continuous values
- Decision Trees: Create a model that predicts target values
- Support Vector Machines: Effective for classification tasks
- Random Forest: Combines multiple decision trees
- Neural Networks: Inspired by biological neural networks

2. Unsupervised Learning
Unsupervised learning finds hidden patterns in data without labeled examples. The algorithm must discover the structure in the data on its own.

Examples include:
- Clustering: Grouping similar data points together
- Association: Finding relationships between variables
- Dimensionality Reduction: Simplifying data while preserving information

Common unsupervised learning algorithms:
- K-Means Clustering: Groups data into k clusters
- Hierarchical Clustering: Creates tree-like cluster structures
- Principal Component Analysis (PCA): Reduces data dimensions
- DBSCAN: Density-based clustering algorithm

3. Reinforcement Learning
Reinforcement learning involves an agent learning to make decisions by taking actions in an environment to maximize cumulative reward.

Key concepts include:
- Agent: The learner or decision maker
- Environment: The world the agent interacts with
- Actions: What the agent can do
- Rewards: Feedback from the environment
- Policy: The strategy the agent uses

Applications of reinforcement learning:
- Game playing (Chess, Go, video games)
- Robotics and autonomous systems
- Trading algorithms and financial modeling
- Recommendation systems

Neural Networks and Deep Learning

Neural networks are computational models inspired by biological neural networks. They consist of interconnected nodes (neurons) organized in layers.

Basic structure:
- Input Layer: Receives the initial data
- Hidden Layers: Process data through weighted connections
- Output Layer: Produces the final result

Each neuron:
- Receives inputs from previous layer neurons
- Applies weights to these inputs
- Adds a bias term
- Passes result through activation function
- Sends output to next layer neurons

Activation functions introduce non-linearity:
- Sigmoid: Maps inputs to values between 0 and 1
- ReLU: Returns max(0, x), most commonly used
- Tanh: Maps inputs to values between -1 and 1
- Softmax: Used in output layer for classification

Deep learning uses neural networks with multiple hidden layers. The term "deep" refers to the number of layers in the network.

Training Process:
1. Forward Pass: Input data flows through network
2. Loss Calculation: Compare predicted output with actual target
3. Backward Pass: Calculate gradients using backpropagation
4. Weight Update: Adjust weights to minimize loss

Common deep learning architectures:
- Feedforward Networks: Information flows in one direction
- Convolutional Neural Networks (CNNs): Designed for image processing
- Recurrent Neural Networks (RNNs): Handle sequential data
- Long Short-Term Memory (LSTM): Improved RNN for long sequences
- Transformer Networks: Use attention mechanisms

Applications of Machine Learning:

Healthcare:
- Medical image analysis and diagnosis
- Drug discovery and development
- Personalized treatment recommendations
- Epidemic prediction and tracking

Finance:
- Fraud detection and prevention
- Algorithmic trading strategies
- Credit scoring and risk assessment
- Market analysis and prediction

Technology:
- Search engines and information retrieval
- Recommendation systems
- Computer vision and image recognition
- Natural language processing

Transportation:
- Autonomous vehicles and self-driving cars
- Route optimization and traffic management
- Predictive maintenance for vehicles
- Smart traffic control systems

Challenges in Machine Learning:

Data Quality:
- Ensuring data is accurate and representative
- Handling missing or incomplete data
- Dealing with biased or skewed datasets
- Data privacy and security concerns

Model Performance:
- Overfitting: Model learns training data too well
- Underfitting: Model is too simple to capture patterns
- Generalization: Ensuring model works on new data
- Interpretability: Understanding how models make decisions

Computational Resources:
- Training large models requires significant computing power
- Storage requirements for big datasets
- Real-time processing constraints
- Energy consumption and environmental impact

The field of machine learning continues to evolve rapidly with new techniques, algorithms, and applications emerging regularly. Understanding these fundamental concepts provides a solid foundation for exploring advanced topics in artificial intelligence and data science.
"""
    
    # Insert content
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    # Save PDF
    filename = "ML_Demo_for_Quiz.pdf"
    doc.save(filename)
    doc.close()
    
    print(f"✅ Created demo PDF: {filename}")
    print("This PDF contains machine learning content perfect for automatic quiz generation!")
    print("\nContent includes:")
    print("• Machine Learning types (Supervised, Unsupervised, Reinforcement)")
    print("• Neural Networks and Deep Learning")
    print("• Algorithms and Applications")
    print("• Perfect for testing 4-option multiple choice questions")

if __name__ == "__main__":
    create_demo_pdf()
