"""
Demo: What happens when you click "Start Quiz"
Shows actual quiz questions and options generated from educational PDFs
"""

import streamlit as st
import random

def demo_quiz_questions():
    """Demo questions that would be generated from educational PDFs"""
    
    # Sample questions that AI would generate from different educational PDFs
    sample_questions = [
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "Q1: What mathematical concept is explained in this section?",
            "context": "A linear equation is an equation that makes a straight line when graphed. The standard form is y = mx + b, where m is the slope (rate of change) and b is the y-intercept (where the line crosses the y-axis).",
            "options": [
                "Algebraic equations and problem solving",
                "Chemical reaction mechanisms", 
                "Historical timeline analysis",
                "Literary character development"
            ],
            "correct_answer": 0,
            "source": "Mathematics_Fundamentals.pdf",
            "explanation": "This section discusses linear equations, which are fundamental algebraic concepts used in mathematics."
        },
        {
            "id": 2,
            "type": "multiple_choice", 
            "question": "Q2: What Python programming concept is explained in this section?",
            "context": "In Python, a list is an ordered collection that can contain different data types. You can add items using append(), remove items using remove(), and access items by index like my_list[0].",
            "options": [
                "Database optimization methods",
                "Python syntax and programming fundamentals",
                "HTML markup structure", 
                "CSS styling properties"
            ],
            "correct_answer": 1,
            "source": "Python_Programming_Guide.pdf",
            "explanation": "This question focuses on Python data structures, specifically lists and their methods, which are fundamental Python concepts."
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "Q3: What physics principle is described in this content?",
            "context": "Newton's First Law states that an object at rest stays at rest, and an object in motion stays in motion, unless acted upon by an external force. This is also known as the law of inertia.",
            "options": [
                "Mathematical algebraic concepts",
                "Historical political systems",
                "Physical laws and natural phenomena", 
                "Literary writing techniques"
            ],
            "correct_answer": 2,
            "source": "Science_Fundamentals.pdf",
            "explanation": "This describes Newton's laws of motion, fundamental principles in physics that govern how objects move."
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "Q4: What JavaScript concept is described here?",
            "context": "JavaScript functions can be declared using the function keyword, or as arrow functions using =>. Functions are first-class objects and can be passed as arguments to other functions.",
            "options": [
                "JavaScript programming and web development",
                "Python data structures",
                "Mathematical calculus",
                "Historical timeline events"
            ],
            "correct_answer": 0,
            "source": "JavaScript_Programming_Guide.pdf", 
            "explanation": "This question tests understanding of JavaScript functions and functional programming concepts."
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "Q5: What historical period is described here?",
            "context": "The Renaissance was a 'rebirth' of classical learning and culture, characterized by humanism and artistic innovation during the 14th-17th centuries in Europe.",
            "options": [
                "Mathematical problem-solving methods",
                "Scientific experimental procedures", 
                "Programming language syntax",
                "Historical events and civilizations"
            ],
            "correct_answer": 3,
            "source": "World_History_Overview.pdf",
            "explanation": "This question tests knowledge of the Renaissance period, a major era in European history."
        }
    ]
    
    return sample_questions

def main():
    st.set_page_config(
        page_title="Quiz Demo - What You See When You Click Start Quiz",
        page_icon="🎯",
        layout="wide"
    )
    
    # Custom CSS for clear display
    st.markdown("""
    <style>
    .quiz-question {
        background-color: #f8f9fa;
        border: 2px solid #007bff;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .question-header {
        color: #2c3e50;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .context-box {
        background-color: #e9ecef;
        border-left: 4px solid #007bff;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .option-correct {
        background-color: #d4edda;
        border: 2px solid #28a745;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    
    .option-wrong {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    
    .option-normal {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    # 🎯 QUIZ DEMO: What You See When You Click "Start Quiz"
    
    ## ✅ This is exactly what happens when you click "🚀 Start Quiz" in StudyMate!
    """)
    
    st.info("📚 **Context:** You've uploaded educational PDFs and clicked 'Start Quiz' with 5 questions selected.")
    
    # Initialize session state
    if 'demo_current_question' not in st.session_state:
        st.session_state.demo_current_question = 0
    if 'demo_answers' not in st.session_state:
        st.session_state.demo_answers = {}
    if 'demo_quiz_completed' not in st.session_state:
        st.session_state.demo_quiz_completed = False
    
    questions = demo_quiz_questions()
    
    if not st.session_state.demo_quiz_completed:
        current_q = st.session_state.demo_current_question
        
        if current_q < len(questions):
            question = questions[current_q]
            
            # Progress bar
            progress = (current_q + 1) / len(questions)
            st.progress(progress)
            st.markdown(f"### Question {current_q + 1} of {len(questions)}")
            
            # Question display
            st.markdown(f"""
            <div class="quiz-question">
                <div class="question-header">{question['question']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Source information
            st.markdown(f"**📄 Source Document:** {question['source']}")
            
            # Context from PDF
            st.markdown("**📖 Context from your PDF:**")
            st.markdown(f"""
            <div class="context-box">
                {question['context']}
            </div>
            """, unsafe_allow_html=True)
            
            # Answer options
            st.markdown("**🎯 Choose the correct answer (4 options, 1 correct):**")
            
            # Display options as radio buttons
            answer = st.radio(
                "Select your answer:",
                question['options'],
                key=f"demo_q_{current_q}",
                index=None
            )
            
            # Show how AI generated this question
            with st.expander("ℹ️ How this question was generated by AI"):
                st.write(f"• **AI Analysis:** This question was automatically generated from your PDF content")
                st.write(f"• **Source:** Extracted from '{question['source']}'")
                st.write(f"• **Method:** AI identified key concepts and created multiple-choice options")
                st.write(f"• **Pattern Recognition:** AI detected educational content and matched it to appropriate question templates")
            
            # Navigation buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if current_q > 0:
                    if st.button("⬅️ Previous Question"):
                        st.session_state.demo_current_question -= 1
                        st.rerun()
            
            with col2:
                if answer:
                    if st.button("💾 Save Answer"):
                        st.session_state.demo_answers[current_q] = answer
                        st.success("✅ Answer saved!")
            
            with col3:
                if current_q < len(questions) - 1:
                    if st.button("➡️ Next Question"):
                        if answer:
                            st.session_state.demo_answers[current_q] = answer
                            st.session_state.demo_current_question += 1
                            st.rerun()
                        else:
                            st.warning("Please select an answer first!")
                else:
                    if st.button("🏁 Finish Quiz"):
                        if answer:
                            st.session_state.demo_answers[current_q] = answer
                            st.session_state.demo_quiz_completed = True
                            st.rerun()
                        else:
                            st.warning("Please select an answer first!")
    
    else:
        # Quiz completed - show results
        st.markdown("## 🎉 Quiz Completed!")
        st.balloons()
        
        # Calculate score
        correct_count = 0
        for i, question in enumerate(questions):
            user_answer = st.session_state.demo_answers.get(i, "")
            correct_option = question['options'][question['correct_answer']]
            if user_answer == correct_option:
                correct_count += 1
        
        score_percentage = (correct_count / len(questions)) * 100
        
        # Display results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Score", f"{correct_count}/{len(questions)}")
        with col2:
            st.metric("📈 Percentage", f"{score_percentage:.1f}%")
        with col3:
            if score_percentage >= 80:
                st.metric("🏆 Grade", "Excellent!")
            elif score_percentage >= 60:
                st.metric("👍 Grade", "Good!")
            else:
                st.metric("📚 Grade", "Keep studying!")
        
        # Detailed results
        st.markdown("### 📋 Detailed Question Review with Correct Answers")
        
        for i, question in enumerate(questions):
            user_answer = st.session_state.demo_answers.get(i, "No answer")
            correct_option = question['options'][question['correct_answer']]
            is_correct = user_answer == correct_option
            
            with st.container():
                if is_correct:
                    st.markdown(f"#### ✅ Question {i+1}: CORRECT")
                    st.success("You got this right!")
                else:
                    st.markdown(f"#### ❌ Question {i+1}: INCORRECT")
                    st.error("Review the correct answer below")
                
                st.markdown(f"**Question:** {question['question']}")
                st.markdown(f"**📄 Source:** {question['source']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("**🎯 Your Answer:**")
                    if is_correct:
                        st.success(f"✅ {user_answer}")
                    else:
                        st.error(f"❌ {user_answer}")
                
                with col_b:
                    st.markdown("**✅ Correct Answer:**")
                    st.success(f"✅ {correct_option}")
                
                st.markdown("**💡 Explanation:**")
                st.info(question['explanation'])
                
                st.markdown("---")
        
        # Reset button
        if st.button("🔄 Take New Quiz"):
            st.session_state.demo_current_question = 0
            st.session_state.demo_answers = {}
            st.session_state.demo_quiz_completed = False
            st.rerun()
    
    # Information about the real system
    st.markdown("---")
    st.markdown("## 🚀 This is exactly what you get in StudyMate!")
    
    st.info("""
    **🎯 In the real StudyMate application:**
    - Upload your own PDF study materials
    - AI analyzes YOUR content and generates questions
    - Questions are based on YOUR specific documents
    - Same interface and experience as shown above
    - Access at: http://localhost:8518
    """)

if __name__ == "__main__":
    main()
