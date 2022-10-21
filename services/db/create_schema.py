from tortoise import Tortoise, run_async
from database.connect_database import connect_database

async def main():
    await connect_database()
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(main())