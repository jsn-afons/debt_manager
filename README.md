# Debt Collector (DebtTracker)

A simple Flask application to help you keep track of who owes you money.
![Dashboard Screenshot](/static/dashboard_screenshot.png)

## Why I Built This
After completing my "100 Days of Python," I wanted to build something real. My brother often complained about losing track of money he lent to friends—forgetting amounts or due dates. I built this tool specifically to solve that problem for him (and anyone else who needs it!).

## Key Features
*   **Dashboard**: A quick overview of total money owed to you and how much you've recovered.
*   **Partial Payments**: Life happens! If someone can only pay back half right now, you can log a partial payment, and the app automatically updates the remaining balance.
*   **History Log**: Every action is recorded. Did John pay $50 last week? Check the history tab to see a Sentence-based sentence log of exactly what happened.
*   **Debtors List**: A dedicated page to see everyone who currently owes you.

## How to Run It
You can run this project locally on your machine.

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**:
    ```bash
    python main.py
    ```

3.  **Open in Browser**:
    Go to `http://127.0.0.1:5000` in your web browser.

## Tech Stack
*   **Python (Flask)**: Backend logic.
*   **SQLAlchemy**: Database management.
*   **Bootstrap**: For the user interface handling.
*   **Jinja2**: Templating engine.

## Contact Me
I'm Jason Afons, a Python Developer.

*   **Email**: [jafons2@gmail.com](mailto:jafons2@gmail.com)
*   **LinkedIn**: [Jason Afons](https://www.linkedin.com/in/jasonafons/)
