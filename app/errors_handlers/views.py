import logging
from http import HTTPStatus

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic.v1.error_wrappers import display_errors  # todo remove use of v1
from sqlalchemy.exc import SQLAlchemyError
from starlette.authentication import AuthenticationError

from app.core.config import settings


def _get_logger() -> logging.Logger:
    return logging.getLogger(settings.LOGGER_NAME)


def authentication_handler(_: Request, exc: AuthenticationError) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.UNAUTHORIZED,
        content={"detail": 'Failed to authenticate'}
    )


def db_error(_: Request, exc: SQLAlchemyError) -> JSONResponse:
    _get_logger().critical(f'Error in database ({exc.__class__.__name__}): {exc}')
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"detail": f'An unexpected error occurred. We are already working on fixing it'}
    )


def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    _get_logger().warning(f'Form validation error: {display_errors(exc.errors())}')
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": display_errors(exc.errors())},
    )


def internal_server_error_handler(_: Request, exc: Exception) -> JSONResponse:
    _get_logger().critical(f'Unhandled error ({exc.__class__.__name__}): {exc}')
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"detail": f"An unexpected error occurred. We are already working on fixing it"}
    )
