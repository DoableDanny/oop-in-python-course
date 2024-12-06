from document_states import DocumentStates
from user_roles import UserRoles
from document import Document

# Create a document in the DRAFT state with an EDITOR role
doc = Document(DocumentStates.DRAFT, UserRoles.EDITOR)
print(f"Initial state: {doc.state.name}")

# Try publishing as an EDITOR
doc.publish()
print(f"State after publishing: {doc.state.name}")

# Change user role to ADMIN and publish again
doc.current_user_role = UserRoles.ADMIN
doc.publish()
print(f"State after admin publishes: {doc.state.name}")