import uuid


# generate unique identifier
def generate_id(id=uuid.uuid4):
    return str(id().int)
