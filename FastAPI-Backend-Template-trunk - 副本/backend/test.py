import asyncpg
import asyncio

async def test_connection():
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='123456',
            database='myfastapi',
            host='127.0.0.1',
            port=5432
        )
        await conn.close()
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")

asyncio.run(test_connection())