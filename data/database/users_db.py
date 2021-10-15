import aiosqlite as lite

data = 'data/database/data.db'


async def add_new_user(user_id: int, user_name: str):
    async with lite.connect(data) as con:
        cur = await con.cursor()
        await cur.execute("SELECT user_id FROM tbl_users WHERE user_id = ?", (user_id,))

        if not (user_id,) in await cur.fetchall():
            await cur.execute("INSERT INTO tbl_users(user_id, user_name)"
                              "VALUES(?, ?)",
                              (user_id, user_name))
            await con.commit()

