"""
- The state is a shared data structure that holds the current information or context
  of an application.

- In simple terms, it is like the application's memory, keeping track of the variables
  and data that nodes can access and modify as they execute.

Analogy:
Whiteboard in a meeting room: 
The node is a person, writing and reading from the whiteboard. The whiteboard represents the state, where everyone can see and update the information.

"""

"""
- Node are individual function or operations that perform specific tasks within the graph.

- Each node receives input (often the current state), process it, and produces an output or an updated state.

Analogy:
Assembly line in a factory:
Each worker (node) performs a specific task on the product (state). The product moves along the assembly line, and each worker contributes to its transformation, such as, attach a part, paint it, inspect quality and so on.

"""

"""
- Graph in LangGraph is the overaching structure that maps out how different tasks(nodes) are connected and executed

- It visually represents the workflow, showing the sequence and conditional paths between various operations.
"""