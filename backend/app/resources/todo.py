from flask_restful import Resource, reqparse
from app.models.todo import Todo
from app.extensions import db
from app.utils import require_auth

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title is required')
parser.add_argument('description', type=str)
parser.add_argument('completed', type=bool)

class TodoList(Resource):
    def get(self):
        if not user:
            return {'message': 'Unauthorized'}, 401
            
        todos = Todo.query.filter_by(user_id=user.id).all()
        return [todo.to_dict() for todo in todos]

    def post(self):
        if not user:
            return {'message': 'Unauthorized'}, 401
            
        args = parser.parse_args()
        todo = Todo(
            title=args['title'],
            description=args.get('description'),
            completed=args.get('completed', False),
            user_id=user.id
        )
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict(), 201

class TodoItem(Resource):
    def get(self, todo_id):
        if not user:
            return {'message': 'Unauthorized'}, 401
            
        todo = Todo.query.get_or_404(todo_id)
        if todo.user_id != user.id:
            return {'message': 'Unauthorized'}, 403
            
        return todo.to_dict()

    def put(self, todo_id):
        user = verify_clerk_token()
        if not user:
            return {'message': 'Unauthorized'}, 401
            
        todo = Todo.query.get_or_404(todo_id)
        if todo.user_id != user.id:
            return {'message': 'Unauthorized'}, 403
            
        args = parser.parse_args()
        todo.title = args['title']
        if args.get('description') is not None:
            todo.description = args['description']
        if args.get('completed') is not None:
            todo.completed = args['completed']
        
        db.session.commit()
        return todo.to_dict()

    def delete(self, todo_id):
        user = verify_clerk_token()
        if not user:
            return {'message': 'Unauthorized'}, 401
            
        todo = Todo.query.get_or_404(todo_id)
        if todo.user_id != user.id:
            return {'message': 'Unauthorized'}, 403
            
        db.session.delete(todo)
        db.session.commit()
        return '', 204
