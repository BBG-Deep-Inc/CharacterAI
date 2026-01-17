from sqlalchemy import Table,Column,MetaData,String

metadata_obj = MetaData()

character_table = Table(
    "character_table",
    metadata_obj,
    Column("username",String),
    Column("name",String),
    Column("promt",String),
    Column("id",String,primary_key=True)
)