import streamlit as st
import time

# Define the MCQs
mcq = {
    "Which of the following is the capital of India?":{
    "options": ["A. Mumbai", "B. Delhi", "C. Bangalore", "D. Chennai"],
    "answer": "B"
    },
    "What is the name of the first Indian woman to win a Nobel Prize?":{
    "options": ["A. Louis Dreyfus", "B. Marie Antoinette", "C. Mary Shelley", "D. Elizabeth Bennett"],
    "answer": "B"
    },
    "The Renaissance period lasted from which year to which year?":{
    "options": ["A. 1500-1600", "B. 1600-1700", "C. 1700-1800", "D. 1800-1900"],
    "answer": "D"
    },
    "Which country is home to the world's largest lake, Lake Baikal?":{
    "options": ["A. China", "B. India", "C. Russia", "D. Mongolia"],
    "answer": "D"
    },
    "The Battle of Waterloo took place in which year?":{
    "options": ["A. 1688", "B. 1704", "C. 1715", "D. 1716"],
    "answer": "C"
    },
    "What is the Big-O time complexity of binary search?":{
        "options": ["A. O(log n)", "B. O(n)", "C. O(n log n)", "D. O(1)"],
        "answer": "A"
    },
    "Who proposed the Theory of Relativity?":{
        "options": ["A. Albert Einstein", "B. Thomas Edison", "C. Nikola Tesla", "D. Aman Pandey"],
        "answer": "A"
    },
    "Which data structure uses the LIFO (Last In, First Out) principle?":{
        "options": ["A. Array","B. Stack", "C. Queue", "D. Linked List"],
        "answer": "B"
    },
    "The Earth is the third planet from the Sun.":{
        "options": ["A. True", "B. False"],
        "answer": "A"
    },
    "HTML is a programming language.":{
        "options": ["A. True", "B. False"],
        "answer": "B"
    },
    "In Java, the keyword this refers to the current object.":{
        "options": ["A. True", "B. False"],
        "answer": "A"
    }
}

# Main App Function
def main():
    st.set_page_config(page_title="Quiz Game", layout="wide")
    st.title("🎯 Welcome to the Quiz Game")
    st.sidebar.title("Quiz Menu")
    st.sidebar.markdown("Use the menu to navigate through the quiz options.")

    # Sidebar menu
    menu = st.sidebar.radio("Navigate", ["Start Quiz", "Add Question", "Remove Question"])

    if menu == "Start Quiz":
        st.header("📝 Start the Quiz")
        if "quiz_state" not in st.session_state:
            st.session_state.quiz_state = {
                "quiz_started": False,
                "current_score": 0,
                "answered_questions": set()
            }

        if not st.session_state.quiz_state["quiz_started"]:
            if st.button("Start Quiz"):
                st.session_state.quiz_state["quiz_started"] = True
                st.session_state.quiz_state["current_score"] = 0
                st.session_state.quiz_state["answered_questions"] = set()

        if st.session_state.quiz_state["quiz_started"]:
            total_score = len(mcq)
            for question, details in mcq.items():
                if question not in st.session_state.quiz_state["answered_questions"]:
                    st.subheader(f"❓ {question}")
                    user_input = st.radio(f"Options:", details["options"], key=question)
                    submit_placeholder = st.empty()
                    if submit_placeholder.button(f"Submit Answer", key=f"btn_{question}"):
                        with st.spinner("Submitting your answer..."):
                            time.sleep(1)  # Simulates the submission animation
                            if user_input.split(".")[0] == details["answer"]:
                                st.success("Correct! ✅")
                                st.session_state.quiz_state["current_score"] += 1
                            else:
                                st.error("Incorrect! ❌")
                            st.session_state.quiz_state["answered_questions"].add(question)
                            submit_placeholder.empty()
            st.write(f"**Your total score so far: {st.session_state.quiz_state['current_score']}/{total_score}**")
            if len(st.session_state.quiz_state["answered_questions"]) == total_score:
                st.success(f"🎉 Your final score is {st.session_state.quiz_state['current_score']}/{total_score}")
                if st.button("Restart Quiz"):
                    st.session_state.quiz_state = {
                        "quiz_started": False,
                        "current_score": 0,
                        "answered_questions": set()
                    }

    elif menu == "Add Question":
        st.header("➕ Add a New Question")
        question = st.text_input("Enter the question:")
        options = [st.text_input(f"Option {label}:", key=f"opt_{label}") for label in ["A", "B", "C", "D"]]
        answer = st.selectbox("Select the correct answer:", ["A", "B", "C", "D"])
        
        if st.button("Add Question"):
            if question and all(options) and answer:
                mcq[question] = {"options": [f"{chr(65+i)}. {opt}" for i, opt in enumerate(options)], "answer": answer}
                st.success("✅ Question added successfully!")
            else:
                st.error("❌ Please complete all fields before submitting.")

    elif menu == "Remove Question":
        st.header("🗑 Remove an Existing Question")
        if mcq:
            question_to_remove = st.selectbox("Select a question to remove:", list(mcq.keys()))
            if st.button("Remove Question"):
                if question_to_remove in mcq:
                    del mcq[question_to_remove]
                    st.success("✅ Question removed successfully!")
                else:
                    st.error("❌ Question not found!")
        else:
            st.info("No questions available to remove.")

if __name__ == "__main__":
    main()
