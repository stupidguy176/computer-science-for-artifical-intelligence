
## Knowledge

- [Lecture Video](https://www.youtube.com/watch?v=HWQLez87vqM&list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm&index=3)
- [Lecture Notes (2024)](https://cs50.harvard.edu/ai/2024/notes/1/)
- [Lecture Slides (PDF)](https://cdn.cs50.net/ai/2020/spring/lectures/1/lecture1.pdf)
- [Lecture Transcript (SRT)](https://cdn.cs50.net/ai/2020/spring/lectures/1/lang/en/lecture1.srt)
- [Lecture Transcript (Text)](https://cdn.cs50.net/ai/2020/spring/lectures/1/lang/en/lecture1.txt)
- [Quiz 1](https://cs50.harvard.edu/ai/2024/quizzes/1/)
- [Project 1](https://cs50.harvard.edu/ai/2024/projects/1/)

## Keywords

- Model Checking
- Inference Rules
- Conversion to CNF (Conjunctive Normal Form)
- Inference by Resolution
- First-Order Logic

## My Notes

### Information

#### Basic Concepts

- **Sentence**: An assertion about the world in a knowledge representation language.
- **Propositional Logic**:
  - **Proposition Symbols**: `P`, `Q`, `R`
  - **Logical Connectives**: not, and, or, implication, biconditional

##### Implication Truth Table

| P     | Q     | P → Q  |
|-------|-------|--------|
| false | false | true   |
| false | true  | true   |
| true  | false | false  |
| true  | true  | true   |

##### Biconditional Truth Table

| P     | Q     | P ↔ Q  |
|-------|-------|--------|
| false | false | true   |
| false | true  | false  |
| true  | false | false  |
| true  | true  | true   |

- **Model**: Assignment of a truth value to every propositional symbol.
- **Knowledge Base**: A set of sentences known by a knowledge-based agent.
- **Entailment**: In every model in which sentence α is true, sentence β is also true.
- **Inference**: The process of deriving new sentences from old ones using inference algorithms.

#### Model Checking

- A way to verify whether a knowledge base entails a query by checking all possible models.
- Often used in simple scenarios but inefficient for large variable spaces.

#### Knowledge Engineering

- The process of encoding a real-world problem using propositional symbols and logic to represent it computationally.

#### Inference Rules

Used to derive new facts from known ones.

- Modus Ponens
- And Elimination
- Double Negation Elimination
- Implication Elimination
- Biconditional Elimination
- De Morgan's Laws
- Distributive Property

#### Search Problems

1. Initial State  
2. Actions  
3. Transition Model  
4. Goal Test  
5. Path Cost Function

#### Theorem Proving as a Search Problem

- **Initial State**: Starting knowledge base  
- **Actions**: Inference rules  
- **Transition Model**: New knowledge base after inference  
- **Goal Test**: Check if the desired statement is proven  
- **Path Cost Function**: Number of steps in proof  

#### Conversion to CNF

To convert a logical sentence to Conjunctive Normal Form:

1. Eliminate biconditionals
2. Eliminate implications
3. Apply De Morgan’s Laws to move `not` inwards
4. Use the distributive law

#### Inference by Resolution

- An alternative inference method that avoids model enumeration.
- Proves statements by deriving contradictions.
- If a contradiction is found, the original knowledge entails the statement.

#### First-Order Logic

- Extends propositional logic with **constants** (objects) and **predicates** (relations/functions).
- Allows expression of more complex knowledge structures.

##### Quantification

- **Universal Quantification (∀x)**: Statement is true for all values of x.
- **Existential Quantification (∃x)**: Statement is true for at least one value of x.

### Conclusion

Different types of logic allow different levels of expressive power:

- Propositional Logic
- First-Order Logic
- Second-Order and Higher-Order Logic

These systems aim to allow AI to:

- Represent knowledge
- Reason and draw conclusions (inference)
- Make decisions under certainty or uncertainty

Future topics will explore handling **uncertainty** in AI.
