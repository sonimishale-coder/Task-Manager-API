
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Task
from flask_jwt_extended import jwt_required, get_jwt_identity

tasks_bp = Blueprint("tasks", __name__)


# Create Task
@tasks_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json() or {}

    if not data.get("title"):
        return jsonify({"message": "Task title is required"}), 400

    user_id = int(get_jwt_identity())

    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created successfully"}), 201


# Get All Tasks
@tasks_bp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())

    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        }
        for task in tasks
    ]), 200


# Update Task
@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    user_id = int(get_jwt_identity())

    task = Task.query.filter_by(
        id=task_id, user_id=user_id
    ).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json() or {}

    if "title" in data:
        if not data["title"]:
            return jsonify({"message": "Title cannot be empty"}), 400
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "completed" in data:
        task.completed = bool(data["completed"])

    db.session.commit()

    return jsonify({"message": "Task updated successfully"}), 200


# Delete Task
@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = int(get_jwt_identity())

    task = Task.query.filter_by(
        id=task_id, user_id=user_id
    ).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200
