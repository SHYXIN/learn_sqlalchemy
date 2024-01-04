-- Running upgrade 33ed676a9ead -> 30b186d404c7

ALTER TABLE cookies RENAME TO new_cookies;

UPDATE alembic_version SET version_num='30b186d404c7' WHERE alembic_version.version_num = '33ed676a9ead';

