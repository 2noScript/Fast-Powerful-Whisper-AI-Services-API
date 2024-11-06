from sqlalchemy import Column, Integer, String, Text, JSON, Enum, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# Define Base class
WorkFlowBase = declarative_base()


# Workflow model
class Workflow(WorkFlowBase):
    __tablename__ = "workflow_workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    trigger_type = Column(Enum("MANUAL", "SCHEDULED", "EVENT", name="workflow_trigger_types"), nullable=False)
    callback_url = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    tasks = relationship("WorkflowTask", back_populates="workflow", cascade="all, delete-orphan")
    notifications = relationship("WorkflowNotification", back_populates="workflow", cascade="all, delete-orphan")


# WorkflowTask model for specific workflow tasks
class WorkflowTask(WorkFlowBase):
    __tablename__ = "workflow_tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String(100), unique=True, nullable=False)
    workflow_id = Column(Integer, ForeignKey("workflow_workflows.id", ondelete="CASCADE"))
    component = Column(String(255), nullable=False)
    parameters = Column(JSON, nullable=True)
    retry_policy = Column(JSON, nullable=True)  # e.g., {"max_retries": 3, "interval": 5}
    timeout = Column(Integer, nullable=True)  # seconds
    delay = Column(Integer, nullable=True)  # seconds
    condition = Column(JSON, nullable=True)  # e.g., {"@IF": {...}, "@THEN": "task_b"}
    status = Column(Enum("PENDING", "RUNNING", "SUCCESS", "FAILED", name="workflow_task_statuses"), nullable=False,
                    server_default="PENDING")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    on_failure = Column(Text, nullable=True)

    # Relationship with Workflow
    workflow = relationship("Workflow", back_populates="tasks")


# WorkflowNotification model for workflow notifications
class WorkflowNotification(WorkFlowBase):
    __tablename__ = "workflow_notifications"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflow_workflows.id", ondelete="CASCADE"))
    channel = Column(String(50), nullable=False)  # Specify length for consistency
    recipient = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)  # Changed to Text for potentially longer messages

    # Relationship with Workflow
    workflow = relationship("Workflow", back_populates="notifications")
