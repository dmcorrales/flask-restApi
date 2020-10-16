from __init__ import ma


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


task_schema = TaskSchema() # Only one 'task'
tasks_schema = TaskSchema(many=True) # Multiple 'task'
