"""
Create sample PDF files for testing StudyMate
"""

import fitz  # PyMuPDF
import os

def create_sample_pdf(filename, title, content):
    """Create a PDF file with the given content"""
    doc = fitz.open()  # Create new PDF
    page = doc.new_page()  # Add a page
    
    # Insert title
    page.insert_text((50, 50), title, fontsize=16, color=(0, 0, 0))
    
    # Insert content
    text_rect = fitz.Rect(50, 80, 550, 750)  # Define text area
    page.insert_textbox(text_rect, content, fontsize=11, color=(0, 0, 0))
    
    # Save the PDF
    doc.save(filename)
    doc.close()
    print(f"Created: {filename}")

def main():
    """Create sample academic PDFs"""
    
    # Sample PDF 1: Machine Learning Basics
    ml_content = """
Machine Learning Fundamentals

Machine learning is a subset of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

Types of Machine Learning:

1. Supervised Learning
Supervised learning uses labeled training data to learn a mapping function from input variables to output variables. The goal is to approximate the mapping function so well that when you have new input data, you can predict the output variables for that data.

Examples of supervised learning include:
- Classification: Predicting categories (spam vs. not spam emails)
- Regression: Predicting continuous values (house prices, stock prices)

Common algorithms: Linear Regression, Decision Trees, Random Forest, Support Vector Machines, Neural Networks

2. Unsupervised Learning
Unsupervised learning finds hidden patterns in data without labeled examples. The system tries to learn without a teacher, finding structure in data where you don't know the outcome.

Examples include:
- Clustering: Grouping similar data points (customer segmentation)
- Association: Finding rules that describe relationships (market basket analysis)
- Dimensionality Reduction: Reducing the number of features while preserving information

Common algorithms: K-Means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA)

3. Reinforcement Learning
Reinforcement learning is an area of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward. The agent learns through trial and error, receiving feedback in the form of rewards or penalties.

Key concepts:
- Agent: The learner or decision maker
- Environment: The world the agent operates in
- Actions: What the agent can do
- Rewards: Feedback from the environment
- Policy: The strategy the agent uses to determine actions

Applications: Game playing (AlphaGo), robotics, autonomous vehicles, recommendation systems

Key Machine Learning Algorithms:

Linear Regression: A statistical method that models the relationship between a dependent variable and independent variables using a linear equation. It's used for predicting continuous values.

Decision Trees: A tree-like model that makes decisions by splitting data based on feature values. Easy to interpret and visualize, making them popular for business applications.

Neural Networks: Computational models inspired by biological neural networks. They consist of interconnected nodes (neurons) that process information through weighted connections.

Support Vector Machines (SVM): Algorithms that find the optimal boundary (hyperplane) to separate different classes of data. Effective for both classification and regression tasks.

Random Forest: An ensemble method that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

The Machine Learning Process:

1. Data Collection: Gathering relevant data for the problem
2. Data Preprocessing: Cleaning and preparing data for analysis
3. Feature Selection: Choosing the most relevant variables
4. Model Selection: Choosing the appropriate algorithm
5. Training: Teaching the model using training data
6. Evaluation: Testing the model's performance
7. Deployment: Implementing the model in production
8. Monitoring: Continuously checking model performance

Applications of Machine Learning:

- Healthcare: Disease diagnosis, drug discovery, personalized treatment
- Finance: Fraud detection, algorithmic trading, credit scoring
- Technology: Search engines, recommendation systems, computer vision
- Transportation: Autonomous vehicles, route optimization
- Marketing: Customer segmentation, targeted advertising, price optimization
- Manufacturing: Quality control, predictive maintenance, supply chain optimization

Challenges in Machine Learning:

- Data Quality: Poor quality data leads to poor models
- Overfitting: Models that perform well on training data but poorly on new data
- Bias: Models that reflect unfair biases present in training data
- Interpretability: Understanding how complex models make decisions
- Scalability: Handling large datasets and real-time processing requirements

Future of Machine Learning:

Machine learning continues to evolve with advances in deep learning, quantum computing, and edge computing. The field is moving toward more automated machine learning (AutoML), better interpretability, and more efficient algorithms that require less data and computational resources.
"""

    # Sample PDF 2: Deep Learning and Neural Networks
    dl_content = """
Deep Learning and Neural Networks

Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to model and understand complex patterns in data. It has revolutionized many fields including computer vision, natural language processing, and speech recognition.

Neural Network Architecture:

A neural network consists of interconnected nodes called neurons, organized in layers:

1. Input Layer
The input layer receives the raw data. Each neuron in this layer represents a feature or attribute of the input data. For example, in image recognition, each neuron might represent a pixel value.

2. Hidden Layers
Hidden layers are between the input and output layers. These layers perform the actual processing and feature extraction. Deep networks have multiple hidden layers, allowing them to learn complex patterns and representations.

3. Output Layer
The output layer produces the final prediction or classification. The number of neurons in this layer depends on the problem type (e.g., one neuron for binary classification, multiple for multi-class classification).

Key Concepts in Neural Networks:

Activation Functions
Activation functions determine the output of a neural network node. They introduce non-linearity into the network, allowing it to learn complex patterns.

Common activation functions:
- ReLU (Rectified Linear Unit): f(x) = max(0, x) - Most popular for hidden layers
- Sigmoid: f(x) = 1/(1 + e^(-x)) - Outputs values between 0 and 1
- Tanh: f(x) = (e^x - e^(-x))/(e^x + e^(-x)) - Outputs values between -1 and 1
- Softmax: Used in output layer for multi-class classification

Weights and Biases
Weights determine the strength of connections between neurons. Biases allow the activation function to shift, providing more flexibility in learning. Both are learned during training through backpropagation.

Backpropagation
Backpropagation is the algorithm used to train neural networks. It works by:
1. Forward pass: Input data flows through the network to produce an output
2. Calculate loss: Compare the output with the expected result
3. Backward pass: Calculate gradients of the loss with respect to weights
4. Update weights: Adjust weights to minimize the loss

Loss Functions
Loss functions measure how well the network's predictions match the actual targets:
- Mean Squared Error (MSE): For regression problems
- Cross-entropy: For classification problems
- Binary Cross-entropy: For binary classification

Optimization Algorithms
These algorithms update the network weights to minimize the loss:
- Gradient Descent: Basic optimization algorithm
- Stochastic Gradient Descent (SGD): Uses random samples for faster training
- Adam: Adaptive learning rate optimization algorithm
- RMSprop: Adaptive learning rate method

Types of Neural Networks:

Feedforward Neural Networks
The simplest type where information flows in one direction from input to output. Good for basic classification and regression tasks.

Convolutional Neural Networks (CNNs)
Specialized for processing grid-like data such as images. Key components:
- Convolutional layers: Apply filters to detect features like edges and patterns
- Pooling layers: Reduce spatial dimensions while preserving important information
- Fully connected layers: Perform final classification

Applications: Image recognition, computer vision, medical imaging

Recurrent Neural Networks (RNNs)
Designed for sequential data like text or time series. They have memory that allows them to use information from previous time steps.

Variants:
- LSTM (Long Short-Term Memory): Better at handling long sequences
- GRU (Gated Recurrent Unit): Simpler alternative to LSTM

Applications: Natural language processing, speech recognition, time series prediction

Transformer Networks
Modern architecture that uses attention mechanisms to process sequential data more efficiently than RNNs. Foundation for models like BERT and GPT.

Training Deep Networks:

Challenges:
- Vanishing Gradients: Gradients become very small in deep networks
- Overfitting: Network memorizes training data instead of learning patterns
- Computational Requirements: Deep networks require significant computing power

Solutions:
- Batch Normalization: Normalizes inputs to each layer
- Dropout: Randomly sets some neurons to zero during training
- Regularization: Adds penalty terms to prevent overfitting
- Transfer Learning: Uses pre-trained models as starting points

Applications of Deep Learning:

Computer Vision:
- Image classification and object detection
- Facial recognition and medical image analysis
- Autonomous vehicle perception systems

Natural Language Processing:
- Machine translation and text summarization
- Chatbots and virtual assistants
- Sentiment analysis and document classification

Speech and Audio:
- Speech recognition and synthesis
- Music generation and audio classification
- Voice assistants and transcription services

Healthcare:
- Medical diagnosis from imaging data
- Drug discovery and development
- Personalized treatment recommendations

Gaming and Entertainment:
- Game AI and procedural content generation
- Recommendation systems for content
- Computer graphics and animation

Future Directions:

- Explainable AI: Making deep learning models more interpretable
- Efficient Architectures: Developing models that require less computation
- Few-shot Learning: Learning from very few examples
- Neuromorphic Computing: Hardware designed to mimic brain structure
- Quantum Machine Learning: Combining quantum computing with neural networks

Deep learning continues to advance rapidly, with new architectures and techniques being developed regularly. The field is moving toward more efficient, interpretable, and generalizable models that can work with less data and computational resources.
"""

    # Create the PDFs
    create_sample_pdf("sample_ml_basics.pdf", "Machine Learning Fundamentals", ml_content)
    create_sample_pdf("sample_deep_learning.pdf", "Deep Learning and Neural Networks", dl_content)
    
    print("\n✅ Sample PDFs created successfully!")
    print("You can now upload these files to test StudyMate:")
    print("- sample_ml_basics.pdf")
    print("- sample_deep_learning.pdf")

if __name__ == "__main__":
    main()
