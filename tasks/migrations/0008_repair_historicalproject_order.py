from django.db import migrations


def add_missing_historicalproject_order(apps, schema_editor):
    table_name = 'tasks_historicalproject'
    column_name = 'order'

    with schema_editor.connection.cursor() as cursor:
        columns = {
            column.name
            for column in schema_editor.connection.introspection.get_table_description(cursor, table_name)
        }

    if column_name in columns:
        return

    quoted_table = schema_editor.quote_name(table_name)
    quoted_column = schema_editor.quote_name(column_name)
    schema_editor.execute(
        f'ALTER TABLE {quoted_table} ADD COLUMN {quoted_column} integer NOT NULL DEFAULT 1'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_project_options_historicalproject_order_and_more'),
    ]

    operations = [
        migrations.RunPython(
            add_missing_historicalproject_order,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
