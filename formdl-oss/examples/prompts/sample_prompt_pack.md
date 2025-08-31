# Sample Prompt Pack (global)

System:
- Extract fields according to schema. Round currency to 2 decimals. Ignore marginal notes.
- If a field is unreadable, set it to null and add a note in `__notes__`.

Field Hints:
- person.name -> Person's full name, text near top-left box.
- person.nin -> UK National Insurance Number (format: AA999999A).
- amount -> Numeric total in GBP.
