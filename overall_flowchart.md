# Program Flowcharts

These flowcharts use Mermaid syntax. GitHub can render Mermaid diagrams in Markdown files.

## 1. Overall Program Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Initialize lists and sets]
    B --> C[Display main menu]
    C --> D[/Read menu choice/]
    D --> E{Valid choice?}
    E -->|1| F[Add student]
    E -->|2| G[Search student]
    E -->|3| H[Update student]
    E -->|4| I[Delete student]
    E -->|5| J[Display all records]
    E -->|6| K[Calculate average]
    E -->|7| L[Find highest scorer]
    E -->|8| M[List by department]
    E -->|9| N[Count students]
    E -->|10| O[Generate reports]
    E -->|11| P([Exit])
    E -->|Other| Q[Display invalid choice]
    F --> C
    G --> C
    H --> C
    I --> C
    J --> C
    K --> C
    L --> C
    M --> C
    N --> C
    O --> C
    Q --> C
```

## 2. Add Student Flowchart

```mermaid
flowchart TD
    A([Start Add Student]) --> B[/Enter roll number/]
    B --> C{Positive integer?}
    C -->|No| B
    C -->|Yes| D{Roll number already exists?}
    D -->|Yes| E[Display duplicate error]
    E --> Z([Return to menu])
    D -->|No| F[/Collect identity and personal details/]
    F --> G[/Enter number of subjects/]
    G --> H{Positive integer?}
    H -->|No| G
    H -->|Yes| I[Repeat for each subject]
    I --> J[/Enter subject, marks, attendance/]
    J --> K{Marks and attendance in range 0-100?}
    K -->|No| J
    K -->|Yes| L{More subjects?}
    L -->|Yes| J
    L -->|No| M[/Enter optional clubs/]
    M --> N[Create student dictionary]
    N --> O[Append student and update sets]
    O --> P[Display success message]
    P --> Z
```

## 3. Search Student Flowchart

```mermaid
flowchart TD
    A([Start Search]) --> B[/Enter roll number/]
    B --> C[Find matching student]
    C --> D{Student found?}
    D -->|Yes| E[Display student profile]
    D -->|No| F[Display not-found message]
    E --> G([Return to menu])
    F --> G
```

## 4. Delete Student Flowchart

```mermaid
flowchart TD
    A([Start Delete]) --> B[/Enter roll number/]
    B --> C[Find matching student]
    C --> D{Student found?}
    D -->|No| E[Display not-found message]
    E --> Z([Return to menu])
    D -->|Yes| F[Display student profile]
    F --> G[/Ask for deletion confirmation/]
    G --> H{Answer is y?}
    H -->|Yes| I[Remove student from students list]
    I --> J[Display deletion success]
    H -->|No| K[Display deletion cancelled]
    J --> Z
    K --> Z
```

## 5. Calculate Average Flowchart

```mermaid
flowchart TD
    A([Start Average Calculation]) --> B[/Enter roll number/]
    B --> C[Find matching student]
    C --> D{Student found?}
    D -->|No| E[Display not-found message]
    E --> Z([Return])
    D -->|Yes| F[Read marks list]
    F --> G{Marks available?}
    G -->|No| H[Display no-marks message]
    H --> Z
    G -->|Yes| I[Calculate total = sum of marks]
    I --> J[Calculate average = total / count]
    J --> K[Display total and average]
    K --> Z
```

## 6. Highest Scorer Flowchart

```mermaid
flowchart TD
    A([Start]) --> B{Any student records?}
    B -->|No| C[Display no-records message]
    C --> Z([Return])
    B -->|Yes| D[Select students with marks]
    D --> E{Any students with marks?}
    E -->|No| F[Display no-marks message]
    F --> Z
    E -->|Yes| G[Set first eligible student as highest]
    G --> H[Calculate next student's average]
    H --> I{Average greater than current highest?}
    I -->|Yes| J[Update highest student and average]
    I -->|No| K[Keep current highest]
    J --> L{More students?}
    K --> L
    L -->|Yes| H
    L -->|No| M[Display highest scorer]
    M --> Z
```

## 7. Notes

- These diagrams represent the logic of the supplied source code at a high level.
- The main program stores data in memory, so all records are lost when the process ends.
- If the source code changes, update the diagrams so they continue to match the implementation.
