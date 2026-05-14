# 📚 Library Management System

> **Universidad Cooperativa de Colombia**
> Data Structures — Final Project
> Pure Python · Object-Oriented Programming · Classical Data Structures

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Academic Objectives](#academic-objectives)
3. [System Description](#system-description)
4. [Data Structures Used](#data-structures-used)
5. [System Workflow and Custom Logic](#system-workflow-and-custom-logic)
6. [Project Structure](#project-structure)
7. [Technical Requirements](#technical-requirements)
8. [Development Roadmap](#development-roadmap)
9. [Teamwork and Collaboration](#teamwork-and-collaboration)
10. [How to Run](#how-to-run)

---

## 🧭 Project Overview

The **Library Management System** is a console-based application developed entirely in **pure Python**, applying **Object-Oriented Programming (OOP)** principles and **manually implemented classical data structures**.

This project serves as the final academic deliverable for the **Data Structures** course. Its primary goal is to demonstrate that data structures are not abstract theoretical concepts, but practical engineering tools that solve real-world problems when applied correctly.

The system simulates the internal operation of a physical bookstore: from registering books and customers, to managing sales, handling returns, rotating sellers, and navigating weekly promotions — all powered exclusively by data structures implemented from scratch.

> **No frameworks. No databases. No external libraries. Pure Python and pure logic.**

---

## 🎯 Academic Objectives

| Objective | Description |
|-----------|-------------|
| Apply classical data structures | Implement and use each structure in a justified, meaningful context |
| Practice OOP in Python | Design modular, reusable classes following OOP principles |
| Simulate a real system | Model a realistic bookstore workflow using only data structures |
| Collaborative development | Work as a team, dividing responsibilities and integrating components |
| Demonstrate critical thinking | Choose the correct structure for each problem, and justify the choice |

The project evaluates the team's ability to:
- Identify which data structure is most appropriate for a given use case
- Implement data structures manually without relying on Python's built-in abstractions
- Integrate multiple structures into a single cohesive system
- Write clean, modular, and well-organized code

---

## 🏛️ System Description

The Library Management System allows users to interact through a **console menu interface**. The system supports the following core operations:

### 📖 Book Management
- Register new books into the catalog
- List all available books
- Search for books by title or author
- Manage normal and discounted price lists

### 👤 Customer Management
- Register new customers dynamically
- Add customers to a waiting queue
- Assign a seller automatically when a customer reaches the front of the queue

### 🧑‍💼 Seller Management
- Register sellers
- Rotate sellers automatically using a circular system
- Ensure fair workload distribution across all registered sellers

### 🛒 Sales Management
- Process sales for attended customers
- Store every completed sale in a historical record
- Cancel sales and track them through a dedicated stack structure

### 🔄 Returns and Cancellations
- Handle canceled or returned sales
- Use a stack to maintain the full reversal history
- Support undo-like operations for sales management

### 📅 Weekly Promotions
- Register weekly promotional offers
- Navigate promotions forward and backward
- Simulate a circular, wrap-around browsing experience

---

## 🗂️ Data Structures Used

Every data structure in this project is **manually implemented from scratch** in Python. No built-in data structure abstractions are used beyond basic Python variables and control flow.

The following table summarizes which structure is used and why:

| # | Data Structure | Module | Applied To | Justification |
|---|----------------|--------|------------|---------------|
| 1 | Simple List | `simple_list.py` | Book catalog | Linear sequential access to the full book inventory |
| 2 | Double List | `double_list.py` | Normal and discounted prices | Two synchronized price lists that must be managed together |
| 3 | Singly Linked List | `singly_linked_list.py` | Dynamic customer registration | Customers are added dynamically; no fixed-size container needed |
| 4 | Doubly Linked List | `doubly_linked_list.py` | Sales history | Allows forward and backward traversal of the full sales record |
| 5 | Stack | `stack.py` | Canceled sales and returns | LIFO logic: the most recent cancellation is always processed first |
| 6 | Queue | `queue.py` | Customer waiting line | FIFO logic: customers are attended in the order they arrived |
| 7 | Circular Singly Linked List | `circular_singly_linked_list.py` | Seller rotation system | Sellers are rotated in a continuous cycle with no defined end |
| 8 | Circular Doubly Linked List | `circular_doubly_linked_list.py` | Weekly promotions navigation | Promotions can be browsed forward and backward in a loop |

---

### 1. 📋 Simple List — Book Catalog

The book catalog is stored in a **simple (array-based) list**. This structure is appropriate because the catalog is accessed sequentially, supports indexed lookups, and books are added in an ordered fashion.

**Operations supported:** add book, remove book, search by index, display all.

---

### 2. 📋📋 Double List — Price Management

The bookstore maintains **two synchronized price lists**: one for regular prices and one for discounted prices. A **double list** (two parallel lists managed together) is used to keep both lists aligned, allowing the system to compare or display both prices for any book simultaneously.

**Operations supported:** add price pair, update discount, retrieve by index, display both lists.

---

### 3. 🔗 Singly Linked List — Customer Registration

Customers are registered **dynamically** over time, without knowing how many will exist in advance. A **singly linked list** allows nodes to be allocated on demand and traversed in insertion order.

**Operations supported:** add customer (head/tail), remove customer, search by ID, traverse all.

---

### 4. 🔗🔗 Doubly Linked List — Sales History

The sales history must support both **forward and backward navigation** (e.g., viewing the most recent sale or going back to older records). A **doubly linked list** provides bidirectional traversal, making it the right choice for this use case.

**Operations supported:** add sale, traverse forward, traverse backward, display history.

---

### 5. 📦 Stack — Canceled Sales and Returns

When a sale is canceled or a return is processed, it is **pushed onto a stack**. Using LIFO (Last In, First Out) logic, the most recently canceled sale is always at the top — making it easy to undo or review recent reversals.

**Operations supported:** push (cancel sale), pop (process return), peek (view latest), is_empty.

---

### 6. 🪑 Queue — Customer Waiting Line

Customers who arrive at the bookstore enter a **waiting queue**. The first customer to arrive is the first to be attended. A **queue** enforces FIFO (First In, First Out) discipline, which mirrors natural service logic.

**Operations supported:** enqueue (customer arrives), dequeue (customer is attended), peek (next in line), is_empty.

---

### 7. 🔄 Circular Singly Linked List — Seller Rotation

Sellers are assigned to customers automatically. The system **rotates through sellers in a continuous loop** so that no seller is skipped and the workload is distributed evenly. A **circular singly linked list** has no natural end node — when the last seller is reached, the system returns to the first one seamlessly.

**Operations supported:** add seller, get next seller (rotation), display all sellers.

---

### 8. 🔄🔄 Circular Doubly Linked List — Weekly Promotions

The bookstore's weekly promotions are stored in a **circular doubly linked list**. Users can navigate promotions **forward or backward** in a loop, wrapping around when they reach either end. This simulates a carousel-style promotion browser.

**Operations supported:** add promotion, navigate forward, navigate backward, display current.

---

## ⚙️ System Workflow and Custom Logic

The Library Management System is not a generic CRUD application. It follows a **custom internal workflow** that connects all data structures into a coherent simulation:

```
Customer arrives
       │
       ▼
 Enters waiting QUEUE
       │
       ▼
 Dequeued when a seller is free
       │
       ▼
 Seller assigned via CIRCULAR ROTATION
       │
       ▼
 Customer selects book from CATALOG (Simple List)
       │
       ▼
 Price checked: normal or discounted (Double List)
       │
       ▼
 Sale is processed and pushed to SALES HISTORY (Doubly Linked List)
       │
       ├──► If sale is canceled → pushed to CANCELLATION STACK (Stack)
       │
       └──► If promotion is active → browsed via CIRCULAR DOUBLY LIST
```

### Key behavioral rules:

- **Customers must wait in the queue** before being attended. The queue enforces arrival order.
- **Sellers are assigned automatically** by rotating through the circular list. No manual assignment is required.
- **Every completed sale is recorded** in the doubly linked list for full historical tracking.
- **Canceled or returned sales are stacked** so that the most recent reversal is always accessible first.
- **Promotions are navigable in both directions**, wrapping around the circular structure endlessly.
- **The system never crashes on empty structures** — every operation checks state before acting.

Each data structure's role is **meaningful and justified** by the operational logic of the system, not chosen arbitrarily.

---

## 📁 Project Structure

The project follows a clean, modular directory layout that separates concerns between the user interface layer, the business logic layer, and the data structures layer.

```
library_system/
│
├── main.py                          ← Application entry point
│
├── frontend/
│   └── menu.py                      ← Console menu interface and user interaction
│
├── backend/
│   ├── models.py                    ← Domain model classes (Book, Customer, Seller, Sale)
│   ├── library_system.py            ← Core system logic and integration layer
│   └── data_structures/
│       ├── simple_list.py           ← Simple list (book catalog)
│       ├── double_list.py           ← Double list (price management)
│       ├── singly_linked_list.py    ← Singly linked list (customer registration)
│       ├── doubly_linked_list.py    ← Doubly linked list (sales history)
│       ├── stack.py                 ← Stack (canceled sales / returns)
│       ├── queue.py                 ← Queue (customer waiting line)
│       ├── circular_singly_linked_list.py   ← Circular singly linked list (seller rotation)
│       └── circular_doubly_linked_list.py   ← Circular doubly linked list (promotions)
```

### Layer Responsibilities

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Entry Point | `main.py` | Launches the application |
| Interface | `frontend/menu.py` | Handles all user input and console output |
| Business Logic | `backend/library_system.py` | Coordinates operations between models and structures |
| Domain Models | `backend/models.py` | Defines the Book, Customer, Seller, and Sale entities |
| Data Structures | `backend/data_structures/` | Self-contained, independently implemented structures |

---

## 🛠️ Technical Requirements

| Requirement | Status |
|-------------|--------|
| Python version | Python 3.8 or higher |
| External libraries | ❌ None required |
| Frameworks | ❌ Not allowed |
| Databases | ❌ Not allowed |
| Web technologies | ❌ Not allowed |
| OOP required | ✅ Mandatory |
| Manual data structure implementation | ✅ Mandatory |
| Console interface | ✅ Required |
| Modular code organization | ✅ Required |

### Running the Project

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd library_system

# Run the application
python main.py
```

No installation steps, no `pip install`, no dependencies. Just Python.

---

## 🗺️ Development Roadmap

The project is developed in **10 sequential phases**. Each phase has a clear objective, defined responsibilities, and expected Git commits. Phases may be worked on in parallel by different team members when there are no dependencies between them.

---

### Phase 1 — Project Structure Setup

**Objective:** Create the complete directory layout and all empty files following the defined project structure.

**Responsibilities:**
- Create `library_system/` root directory
- Create `frontend/` and `backend/` subdirectories
- Create `backend/data_structures/` subdirectory
- Initialize all `.py` files as empty modules
- Create the `README.md` file

**Involved Components:** All directories and files (no logic yet)

**Academic Purpose:** Establish a shared, consistent project layout that all team members can work within from the start.

**Expected Commits:**
```
feat: initialize project directory structure
docs: add README.md with project overview and roadmap
```

---

### Phase 2 — Domain Model Classes

**Objective:** Define the core data entities of the system as Python classes using OOP principles.

**Responsibilities:**
- Create the `Book` class with attributes: `id`, `title`, `author`, `genre`, `year`, `stock`
- Create the `Customer` class with attributes: `id`, `name`, `email`, `phone`
- Create the `Seller` class with attributes: `id`, `name`, `sales_count`
- Create the `Sale` class with attributes: `id`, `book`, `customer`, `seller`, `date`, `price`, `status`
- Add `__str__` and `__repr__` methods to all classes for readable output

**Involved Components:** `backend/models.py`

**Academic Purpose:** Practice class design and attribute modeling as the foundation of an OOP system.

**Expected Commits:**
```
feat: add Book model class with attributes and string representation
feat: add Customer model class
feat: add Seller model class
feat: add Sale model class
```

---

### Phase 3 — Simple List and Double List

**Objective:** Implement the first two data structures that handle book catalog management and price tracking.

**Responsibilities:**
- Implement `SimpleList` class in `simple_list.py`:
  - Internal array-based storage
  - Methods: `add()`, `remove()`, `get()`, `search()`, `display()`, `is_empty()`, `size()`
- Implement `DoubleList` class in `double_list.py`:
  - Two synchronized internal arrays
  - Methods: `add_pair()`, `get_pair()`, `update_discount()`, `display_both()`, `is_empty()`, `size()`

**Involved Components:** `backend/data_structures/simple_list.py`, `backend/data_structures/double_list.py`

**Academic Purpose:** Understand sequential, index-based storage and how two parallel collections can be managed in sync.

**Expected Commits:**
```
feat: implement SimpleList with add, remove, search, and display methods
feat: implement DoubleList with synchronized pair management
```

---

### Phase 4 — Singly Linked List and Doubly Linked List

**Objective:** Implement the two node-based linked list structures for customer registration and sales history.

**Responsibilities:**
- Implement `Node` class for single linkage (next only)
- Implement `SinglyLinkedList` class in `singly_linked_list.py`:
  - Methods: `add_to_head()`, `add_to_tail()`, `remove()`, `search()`, `traverse()`, `is_empty()`
- Implement `DoubleNode` class with `next` and `prev` pointers
- Implement `DoublyLinkedList` class in `doubly_linked_list.py`:
  - Methods: `add_to_tail()`, `remove()`, `traverse_forward()`, `traverse_backward()`, `is_empty()`

**Involved Components:** `backend/data_structures/singly_linked_list.py`, `backend/data_structures/doubly_linked_list.py`

**Academic Purpose:** Understand dynamic memory allocation through nodes, pointer management, and the difference between unidirectional and bidirectional traversal.

**Expected Commits:**
```
feat: implement SinglyLinkedList with node-based dynamic storage
feat: implement DoublyLinkedList with bidirectional traversal
```

---

### Phase 5 — Stack and Queue

**Objective:** Implement the two linear restricted structures that handle cancellation tracking and customer service order.

**Responsibilities:**
- Implement `Stack` class in `stack.py`:
  - Internal linked-node or array-based storage
  - Methods: `push()`, `pop()`, `peek()`, `is_empty()`, `size()`, `display()`
- Implement `Queue` class in `queue.py`:
  - Internal linked-node or array-based storage
  - Methods: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `size()`, `display()`

**Involved Components:** `backend/data_structures/stack.py`, `backend/data_structures/queue.py`

**Academic Purpose:** Understand access-restricted structures and how LIFO and FIFO models apply directly to real-world service scenarios.

**Expected Commits:**
```
feat: implement Stack with LIFO push, pop, and peek operations
feat: implement Queue with FIFO enqueue, dequeue, and peek operations
```

---

### Phase 6 — Circular Linked Lists

**Objective:** Implement the two circular structures that power seller rotation and promotion browsing.

**Responsibilities:**
- Implement `CircularSinglyLinkedList` class in `circular_singly_linked_list.py`:
  - The last node points back to the first
  - Methods: `add()`, `get_next()` (rotation), `remove()`, `display()`, `is_empty()`
- Implement `CircularDoubleNode` with `next` and `prev` pointers
- Implement `CircularDoublyLinkedList` class in `circular_doubly_linked_list.py`:
  - Both ends connect circularly
  - Methods: `add()`, `navigate_forward()`, `navigate_backward()`, `display_current()`, `is_empty()`

**Involved Components:** `backend/data_structures/circular_singly_linked_list.py`, `backend/data_structures/circular_doubly_linked_list.py`

**Academic Purpose:** Understand circular pointer logic, infinite traversal, and its application in rotation systems and carousel-style navigation.

**Expected Commits:**
```
feat: implement CircularSinglyLinkedList for seller rotation system
feat: implement CircularDoublyLinkedList for weekly promotions navigation
```

---

### Phase 7 — Core System Logic Integration

**Objective:** Build the central coordination layer that connects all models and data structures into a working system.

**Responsibilities:**
- Create `LibrarySystem` class in `library_system.py`
- Instantiate all data structures as internal attributes
- Implement high-level methods that combine structures:
  - `register_book()`, `list_books()`, `search_book()`
  - `register_customer()`, `add_customer_to_queue()`
  - `register_seller()`, `assign_next_seller()`
  - `process_sale()`, `cancel_sale()`, `process_return()`
  - `view_sales_history()`, `view_canceled_sales()`
  - `add_promotion()`, `next_promotion()`, `previous_promotion()`

**Involved Components:** `backend/library_system.py`, all `data_structures/` modules, `backend/models.py`

**Academic Purpose:** Practice system integration: connecting independently developed components into a unified, functional application.

**Expected Commits:**
```
feat: add LibrarySystem class with book and customer management methods
feat: add sales processing, cancellation, and return logic to LibrarySystem
feat: add seller rotation and promotion navigation to LibrarySystem
```

---

### Phase 8 — Console Menu Interface

**Objective:** Build the complete user-facing console interface that allows human interaction with the system.

**Responsibilities:**
- Create `ConsoleMenu` class (or equivalent functions) in `frontend/menu.py`
- Implement the main menu with numbered options
- Implement sub-menus for each module: Books, Customers, Sellers, Sales, Returns, Promotions
- Handle user input validation and display informative error messages
- Format output cleanly with separators and headers
- Connect all menu actions to `LibrarySystem` methods

**Involved Components:** `frontend/menu.py`, `backend/library_system.py`

**Academic Purpose:** Understand how a user interface layer interacts with a business logic layer in a clean, decoupled manner.

**Expected Commits:**
```
feat: add main console menu with module navigation
feat: add book management sub-menu and input handling
feat: add customer, seller, and sales sub-menus
feat: add promotions and cancellations menu options
```

---

### Phase 9 — Entry Point Integration

**Objective:** Connect all layers through `main.py` to produce a fully runnable application.

**Responsibilities:**
- Import `LibrarySystem` and `ConsoleMenu` in `main.py`
- Instantiate the system and the menu
- Launch the application loop
- Handle top-level exceptions and graceful exit
- Add a welcome message displayed on startup

**Involved Components:** `main.py`, `frontend/menu.py`, `backend/library_system.py`

**Academic Purpose:** Understand the role of an entry point in a multi-module Python application and how all layers connect.

**Expected Commits:**
```
feat: add main.py entry point with system and menu initialization
feat: add welcome screen and graceful exit handling to main.py
```

---

### Phase 10 — Testing and Bug Fixing

**Objective:** Verify that all system features work correctly across normal and edge-case scenarios.

**Responsibilities:**
- Test each data structure individually (add, remove, traverse, edge cases)
- Test each system operation through the console menu
- Verify correct behavior when structures are empty (no crashes)
- Verify correct behavior with a single element in each structure
- Verify circular structures wrap around correctly
- Fix all identified bugs before final submission
- Review code for clarity and remove unused code

**Involved Components:** All modules

**Academic Purpose:** Practice systematic testing, debugging discipline, and the importance of validating software before delivery.

**Expected Commits:**
```
fix: handle empty queue on customer dequeue attempt
fix: correct circular rotation pointer after seller removal
fix: resolve off-by-one error in doubly linked list backward traversal
chore: remove unused variables and clean up console output formatting
```

---

## 👥 Teamwork and Collaboration

This project is designed for **collaborative development**. The modular structure allows multiple team members to work independently on different components and integrate them at defined checkpoints.

### Suggested Task Division

| Member | Responsibility |
|--------|----------------|
| Member 1 | Project structure, README, `models.py`, `simple_list.py`, `double_list.py` |
| Member 2 | `singly_linked_list.py`, `doubly_linked_list.py`, customer registration logic |
| Member 3 | `stack.py`, `queue.py`, cancellation and waiting queue logic |
| Member 4 | `circular_singly_linked_list.py`, `circular_doubly_linked_list.py`, rotation and promotion logic |
| All members | `library_system.py` integration, `menu.py`, `main.py`, testing |

> Task division should be adapted based on actual team size. Each member should own their modules entirely — from implementation to testing.

---

### Branch Workflow

```
main
 └── develop
      ├── feature/models
      ├── feature/simple-list
      ├── feature/double-list
      ├── feature/singly-linked-list
      ├── feature/doubly-linked-list
      ├── feature/stack
      ├── feature/queue
      ├── feature/circular-singly-linked-list
      ├── feature/circular-doubly-linked-list
      ├── feature/library-system
      ├── feature/menu
      └── feature/main-entry
```

- All feature branches are created from `develop`
- Once a feature is complete and tested, it is merged back into `develop`
- `main` is updated only when the full system is stable and ready for submission

---

### Commit Conventions

All commits must follow this format:

```
<type>: <short description in English>
```

| Type | When to use |
|------|-------------|
| `feat` | Adding a new feature or component |
| `fix` | Fixing a bug or incorrect behavior |
| `refactor` | Restructuring code without changing behavior |
| `docs` | Updating documentation |
| `chore` | Cleanup, formatting, removing unused code |
| `test` | Adding or fixing test cases |

**Examples:**
```
feat: implement push and pop methods for Stack class
fix: correct tail pointer update in DoublyLinkedList remove method
docs: update README with Phase 6 details
refactor: extract display logic from LibrarySystem into menu.py
chore: remove debug print statements from queue module
```

---

### Collaboration Guidelines

- **Never commit directly to `main`** — always go through a feature branch and `develop`
- **One logical change per commit** — do not bundle unrelated changes in a single commit
- **Write meaningful commit messages** — the message should explain what changed and why
- **Review your own code before pushing** — check for obvious bugs and debug prints
- **Communicate before integrating** — when merging into `develop`, notify the team
- **Keep data structures self-contained** — each module in `data_structures/` should work independently with no imports from other modules in the project

---

## ▶️ How to Run

```bash
# Step 1: Make sure Python 3.8 or higher is installed
python --version

# Step 2: Clone the repository
git clone <repository-url>

# Step 3: Navigate into the project folder
cd library_system

# Step 4: Run the application
python main.py
```

The application will display a welcome screen and a main menu in the console. From there, all system features are accessible through numbered menu options.

---

## 📌 Academic Note

This project is submitted as the **Final Project** for the **Data Structures** course. Its purpose is to demonstrate the practical application of classical data structures inside a realistic, functional software system.

Every structure was chosen based on the specific operational requirements of the bookstore simulation — not for convenience or familiarity. The goal is to show that the right data structure, applied correctly, makes a system more efficient, readable, and logically coherent.

> *"A data structure is not just a way to store data. It is a decision about how your system thinks."*

---

*Library Management System — Data Structures Final Project*
*Pure Python · Object-Oriented Programming · Console Application*
