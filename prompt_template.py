zero_prompt = """
**Instructions: Grade the student's answer based on the given question and reference answer on a scale of 0 to 100. Then identify and list each specific point in the student's answer that leads to point deductions, noting any relevances, accuracies, completenesses, clarities, or areas for improvement compared to the reference answer. Use the following format for the interaction:**

- **Question:** [The question given to the student, which they need to answer succinctly.]
- **Reference Answer:** [A reference answer for comparison.]
- **Student Answer:** [The actual answer provided by the student.]

**Grading Criteria:**

- **Relevance (0-25 points)**: The answer must directly address all parts of the question.
- **Accuracy (0-25 points)**: The answer must be factually correct.
- **Completeness (0-25 points)**: The answer must cover all necessary aspects of the question without omitting crucial details.
- **Clarity (0-25 points)**: The answer must be clearly and logically presented.

**Please provide the feedback as follows:**

1. **Final Score of the Student's Answer:** [0 to 100]
2. **Positive Feedback:** [Highlight strengths and correct aspects of the student's answer.]
3. **Deduction Reason:** [Describe the reason for the deduction, including the number of deduction points. Repeat for each issue identified.]

**Now, let's begin:**

- **Question:** {question}
- **Reference Answer:** {ref_answer}
- **Student Answer:** {stu_answer}

**Feedback:**
"""

one_prompt = """
**Instructions: Grade the student's response based on the given question and reference answer on a scale of 0 to 100. Then identify and list each specific point in the student's answer that leads to point deductions, noting any relevances, accuracies, completenesses, clarities, or areas for improvement compared to the reference answer. Use the following format for the interaction:**

- **Question:** [The question given to the student, which they need to answer succinctly.]
- **Reference Answer:** [A reference answer for comparison.]
- **Student Answer:** [The actual answer provided by the student.]

**Grading Criteria:**

- **Relevance (0-25 points)**: The answer must directly address all parts of the question.
- **Accuracy (0-25 points)**: The answer must be factually correct.
- **Completeness (0-25 points)**: The answer must cover all necessary aspects of the question without omitting crucial details.
- **Clarity (0-25 points)**: The answer must be clearly and logically presented.

**Please provide the feedback as follows:**

1. **Final Score of the Student's Answer:** [0 to 100]
2. **Positive Feedback:** [Highlight strengths and correct aspects of the student's answer.]
3. **Deduction Reason:** [Describe the reason for the deduction, including the number of deduction points. Repeat for each issue identified.]

**Example**:

- **Question:** Explain the primary differences between machine learning and traditional programming.
- **Reference Answer:** In traditional programming, programmers explicitly code the behavior based on logic and data inputs, which the program then executes to produce outputs. Conversely, machine learning involves training a model on a dataset, allowing it to learn the patterns and behaviors from the data, which it then applies to make predictions or decisions, rather than following explicitly programmed instructions.
- **Student Answer:** Traditional programming is where you write specific instructions for a computer to follow. Machine learning instead uses algorithms that learn from data and make decisions based on it.

**Feedback:**

1. **Final Score of the Student's Answer:** 100 - 5 - 15 - 5 = 75
2. **Positive Feedback:** The student correctly identifies that traditional programming involves writing specific instructions, and that machine learning uses algorithms that learn from data to make decisions. The answer is concise and straightforward.
3. **Deduction Reason:** Relevance (5 points deducted) - The student briefly touches on both concepts but does not clearly articulate the key difference in how outputs are generated in traditional programming versus machine learning.
4. **Deduction Reason:** Completeness (15 points deducted) - The answer lacks detail about how machine learning models are trained and use these learnings to make predictions, which is crucial for a full understanding of the differences.
5. **Deduction Reason:** Clarity (5 points deducted) - The explanation could be expanded to better illustrate the contrast between explicitly coded behavior in traditional programming and learned behavior in machine learning.

**Now, let's begin:**

- **Question:** {question}
- **Reference Answer:** {ref_answer}
- **Student Answer:** {stu_answer}

**Feedback:**
"""

few_prompt = """
**Instructions: Grade the student's response based on the given question and reference answer on a scale of 0 to 100. Then identify and list each specific point in the student's answer that leads to point deductions, noting any relevances, accuracies, completenesses, clarities, or areas for improvement compared to the reference answer. Use the following format for the interaction:**

- **Question:** [The question given to the student, which they need to answer succinctly.]
- **Reference Answer:** [A reference answer for comparison.]
- **Student Answer:** [The actual answer provided by the student.]

**Grading Criteria:**

- **Relevance (0-25 points)**: The answer must directly address all parts of the question.
- **Accuracy (0-25 points)**: The answer must be factually correct.
- **Completeness (0-25 points)**: The answer must cover all necessary aspects of the question without omitting crucial details.
- **Clarity (0-25 points)**: The answer must be clearly and logically presented.

**Please provide the feedback as follows:**

1. **Final Score of the Student's Answer:** [0 to 100]
2. **Positive Feedback:** [Highlight strengths and correct aspects of the student's answer.]
3. **Deduction Reason:** [Describe the reason for the deduction, including the number of deduction points. Repeat for each issue identified.]

**Now, let's begin:**

- **Question:** {question}
- **Reference Answer:** {ref_answer}
- **Student Answer:** {stu_answer}

**Feedback:**
"""

prompt_list = [zero_prompt, one_prompt, few_prompt]