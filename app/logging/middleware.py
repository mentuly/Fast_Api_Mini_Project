from fastapi import Request
from .logg import requests_logger
from datetime import datetime

def log_request(request: Request):
    request_time = datetime.now()

    headers = dict(request.headers)
    body = request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    requests_logger.info(
        f"Request Time: {request_time}, Handler: {request.url.path}, Method: {request.method}, "
        f"Headers: {headers}, Body: {body}, User-Agent: {headers.get('user-agent')}"
    )

def request_logging_dependency(request: Request):
    log_request(request)