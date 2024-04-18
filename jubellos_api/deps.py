from fastapi import HTTPException
from fastapi import Security
from fastapi import status
from fastapi.security.api_key import APIKeyHeader
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)
security = HTTPBearer()


def get_api_key(api_key_header: str = Security(api_key_header)):
    if not api_key_header:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


def get_authorization_header(credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Authorization header must start with Bearer")
