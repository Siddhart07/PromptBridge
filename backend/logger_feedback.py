import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def log_feedback_to_mysql(user_input, generated_prompt, routing_info,
                           relevance_score, clarity_score, accuracy_score,
                           edit_effort_score, satisfaction_score,
                           seconds_spent, additional_comments):
    """
    Save feedback data into the MySQL database.
    """
    try:
        # Connect to MySQL Database
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        insert_query = """
            INSERT INTO prompt_feedback (
                user_input,
                generated_prompt,
                detected_intent,
                detected_sub_intent,
                learning_mode,
                relevance_score,
                clarity_score,
                accuracy_score,
                edit_effort_score,
                satisfaction_score,
                seconds_spent,
                additional_comments
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data_tuple = (
            user_input,
            generated_prompt,
            routing_info.get("intent", "Unknown"),
            routing_info.get("sub_intent", "Unknown"),
            routing_info.get("learning_mode", False),
            relevance_score,
            clarity_score,
            accuracy_score,
            edit_effort_score,
            satisfaction_score,
            seconds_spent,
            additional_comments
        )

        cursor.execute(insert_query, data_tuple)
        connection.commit()

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
