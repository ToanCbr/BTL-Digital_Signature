import sqlite3
import shutil
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'digital_signature.db')
DB_PATH = os.path.abspath(DB_PATH)
backup_path = DB_PATH + '.preedit.' + datetime.now().strftime('%Y%m%d_%H%M%S')
shutil.copy2(DB_PATH, backup_path)
print('Backup created at', backup_path)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

try:
    # Work in a transaction
    conn.execute('BEGIN')

    # 1) signed_files: remove ids 1 and 2, keep id 3 and make it id 1
    # We'll copy the desired row into a temp table, clear signed_files, then re-insert with new ids
    cur.execute("CREATE TEMP TABLE keep_signed AS SELECT * FROM signed_files WHERE id=3")
    cur.execute('DELETE FROM signed_files')
    # get columns
    cur.execute("PRAGMA table_info('signed_files')")
    cols = [r[1] for r in cur.fetchall()]
    cols_without_id = [c for c in cols if c != 'id']
    insert_cols = ','.join(cols_without_id)
    placeholders = ','.join('?' for _ in cols_without_id)
    cur.execute(f"INSERT INTO signed_files ({insert_cols}) SELECT {insert_cols} FROM keep_signed")
    # Set id to 1 for the inserted row
    cur.execute('UPDATE signed_files SET id = 1 WHERE ROWID = (SELECT ROWID FROM signed_files LIMIT 1)')
    cur.execute('DROP TABLE keep_signed')

    # 2) signers: delete ids 1,2,3 then renumber remaining rows 4->1,5->2,6->3,7->4
    # We'll select rows with id >=4 ordered by id, then truncate and re-insert with new ids
    cur.execute("CREATE TEMP TABLE keep_signers AS SELECT * FROM signers WHERE id >= 4 ORDER BY id")
    cur.execute('DELETE FROM signers')
    cur.execute("PRAGMA table_info('signers')")
    scols = [r[1] for r in cur.fetchall()]
    scols_without_id = [c for c in scols if c != 'id']
    s_insert_cols = ','.join(scols_without_id)
    s_placeholders = ','.join('?' for _ in scols_without_id)

    # Re-insert rows with new incremental ids
    cur.execute(f"SELECT {s_insert_cols} FROM keep_signers")
    rows = cur.fetchall()
    for new_id, row in enumerate(rows, start=1):
        cur.execute(f"INSERT INTO signers (id, {s_insert_cols}) VALUES (?, {s_placeholders})", (new_id, *row))

    cur.execute('DROP TABLE keep_signers')

    conn.commit()
    print('Database modified successfully')

    # Print resulting tables
    print('\nsigned_files:')
    for r in cur.execute('SELECT * FROM signed_files').fetchall():
        print(r)

    print('\nsigners:')
    for r in cur.execute('SELECT id, name FROM signers ORDER BY id').fetchall():
        print(r)

except Exception as e:
    conn.rollback()
    print('Error:', e)
finally:
    conn.close()
