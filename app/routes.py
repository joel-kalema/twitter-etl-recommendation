from flask import request, jsonify
from sqlalchemy import create_engine, text
from config import Config

def create_routes(app):
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    @app.route('/q2', methods=['GET'])
    def get_recommendations():
        user_id = request.args.get('user_id')
        contact_type = request.args.get('type')
        phrase = request.args.get('phrase')
        hashtag = request.args.get('hashtag')

        with engine.connect() as connection:
            result = connection.execute(text("""
            SELECT user_id, screen_name, description, text 
            FROM users u 
            JOIN tweets t ON u.user_id = t.user_id 
            JOIN interactions i ON t.tweet_id = i.tweet_id 
            WHERE i.contact_user_id = :user_id AND i.type = :contact_type
            AND t.text LIKE :phrase AND EXISTS (
                SELECT 1 FROM hashtags h WHERE h.tweet_id = t.tweet_id AND h.tag = :hashtag
            )
            ORDER BY final_score DESC, u.user_id DESC
            """), {'user_id': user_id, 'contact_type': contact_type, 'phrase': f'%{phrase}%', 'hashtag': hashtag})

            data = result.fetchall()
            response = f"TeamID,1234-0000-0001\n"
            for row in data:
                response += f"{row['user_id']}\t{row['screen_name']}\t{row['description']}\t{row['text']}\n"

        return response
