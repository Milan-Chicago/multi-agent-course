from typing import List, Optional

def are_modalities_compatible(
    client_modalities: Optional[List[str]], agent_modalities: List[str]
) -> bool:
    """Check if the client's accepted modalities are compatible with what the agent supports."""
    if not client_modalities:
        return True  # No specific modalities requested, all are accepted

    for modality in client_modalities:
        if modality in agent_modalities:
            return True

    return False

def new_incompatible_types_error(request_id: int):
    """Create an error response for incompatible modalities."""
    from types2 import JSONRPCResponse, InvalidRequestError

    return JSONRPCResponse(
        id=request_id,
        error=InvalidRequestError(
            message="Incompatible modalities. The agent does not support any of the requested output modalities."
        )
    )