def get_provider_info():
    return {
        'package-name': 'airflow-clickhouse-plugin',
        'name': 'Clickhouse',
        'description': '`Clickhouse <https://clickhouse.com/>`__\n',
        'versions': ['0.8.0'],
        'additional-dependencies': ['apache-airflow>=2.1.0'],
        'integrations': [
            {
                'integration-name': 'Clickhouse',
                'external-doc-url': 'https://github.com/whisklabs/airflow-clickhouse-plugin',
                'how-to-guide': [''],
                'logo': '',
                'tags': ['service'],
            }
        ],
        'operators': [
            {
                'integration-name': 'Clickhouse',
                'python-modules': ['airflow.providers.clickhouse.operators.clickhouse'],
            }
        ],
        'sensors': [
            {
                'integration-name': 'Clickhouse',
                'python-modules': ['airflow.providers.clickhouse.sensors.clickhouse_sql_sensor'],
            }
        ],
        'hooks': [
            {
                'integration-name': 'Clickhouse',
                'python-modules': ['airflow.providers.clickhouse.hooks.clickhouse']
            }
        ],
        'hook-class-names': ['airflow.providers.clickhouse.hooks.clickhouse.ClickHouseHook'],
        'connection-types': [
            {
                'hook-class-name': 'airflow.providers.clickhouse.hooks.clickhouse.ClickHouseHook',
                'connection-type': 'clickhouse',
            }
        ],
    }
