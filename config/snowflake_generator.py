from typing import Annotated

from fastapi import Depends
from snowflake import SnowflakeGenerator

def get_snowflake_generator() -> SnowflakeGenerator:
    return SnowflakeGenerator(0)

snowflake_generator = Annotated[SnowflakeGenerator, Depends(get_snowflake_generator)]