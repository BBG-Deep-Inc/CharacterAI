from sqlalchemy import Column,Table,MetaData,String,Boolean

metadata_obj = MetaData()

table = Table(
    "user_start_table",
    metadata_obj,
    Column("username",String,primary_key=True),
    Column("sub",Boolean)
)