from lib.db import db

class ReplyToActivityUuidStringMigration:
  def migrate_sql():
    data = """
    ALTER TABLE activities DROP COLUMN reply_to_activity_uuid;
    ALTER TABLE activities ADD COLUMN reply_to_activity_uuid uuid;
    """
    return data
  def rollback_sql():
    data = """
    ALTER TABLE activities DROP COLUMN reply_to_activity_uuid;
    ALTER TABLE activities ADD COLUMN reply_to_activity_uuid integer;
    """
    return data
  def migrate():
    db.query_commit(ReplyToActivityUuidStringMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(ReplyToActivityUuidStringMigration.rollback_sql(),{
    })

migration = ReplyToActivityUuidStringMigration