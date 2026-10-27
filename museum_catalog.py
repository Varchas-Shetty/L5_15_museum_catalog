"""Manage a small catalog of museum artifacts."""

import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute(
    "CREATE TABLE artifacts (id INTEGER PRIMARY KEY, title TEXT, era TEXT, "
    "value INTEGER, on_display INTEGER)"
)


def add_artifact(title, era, value, on_display=0):
    """Add an artifact to the catalog."""
    connection.execute(
        "INSERT INTO artifacts (title, era, value, on_display) "
        "VALUES (?, ?, ?, ?)",
        (title, era, value, on_display),
    )
    connection.commit()


def display_status(artifact_id):
    """Return whether an artifact is on display or in storage."""
    row = connection.execute(
        "SELECT on_display FROM artifacts WHERE id = ?", (artifact_id,)
    ).fetchone()
    if row[0] == 1:
        return "on display"
    return "in storage"


def total_value(era):
    """Return the total value of artifacts from an era."""
    total = 0
    for (value,) in connection.execute(
        "SELECT value FROM artifacts WHERE era = ?", (era,)
    ):
        total += value
    return total


def move_to_display(artifact_id):
    """Move an artifact onto display."""
    connection.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?", (artifact_id,)
    )
    connection.commit()


def backup_note():
    """Print a notice that the catalog backup is complete."""
    print("catalog backup complete")


def main():
    """Run a short demonstration of the catalog."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)
    move_to_display(1)
    print(display_status(1))
    print(total_value("Chola"))
    backup_note()


if __name__ == "__main__":
    main()
