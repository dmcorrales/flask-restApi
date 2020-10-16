from flask import Blueprint, request, jsonify
from .model import Task
from .extensions import db
from .service import TaskService
from .schema import task_schema, tasks_schema

main = Blueprint('main', __name__)


@main.route('/')
def main_index():
    return tasks_schema.jsonify(TaskService.findAll(Task))


@main.route('/<id>')
def find_task(id):
    return task_schema.jsonify(TaskService.findById(Task, id))


@main.route('/<id>', methods=['PUT'])
def update_task(id):
    result = TaskService.findById(Task, id)
    title = request.json['title']
    description = request.json['description']
    result.title = title
    result.description = description
    return task_schema.jsonify(TaskService.update(result))


@main.route('/', methods=['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']
    task = Task(title, description)
    TaskService.create(task)
    return task_schema.jsonify(task)


@main.route('/<id>', methods=['DELETE'])
def remove_task(id):
    result = TaskService.findById(Task, id)
    return task_schema.jsonify(TaskService.delete(result))
