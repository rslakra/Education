import os
import boto3
import json

from dotenv import load_dotenv
from mysql import connector

load_dotenv()

try:
    # Connect to RDS
    rds_client = boto3.client('rds')


    db_creds = {
        'host': os.getenv('RDS_HOSTNAME', None),
        'port': os.getenv('RDS_PORT', None),
        'user': os.getenv('RDS_USERNAME', None),
        'database': os.getenv('RDS_DB_NAME', None)
    }

    # db_creds['host'] = 'tod-rds-dev-ue1-backend.proxy-cs1tgvphffrx.us-east-1.rds.amazonaws.com'
    # db_creds['database'] = 'tod'

    print()
    print(f"db_creds={json.dumps(db_creds)}")
    print()

    db_creds['password'] = rds_client.generate_db_auth_token(
        DBHostname=db_creds['host'],
        Port=db_creds['port'],
        DBUsername=db_creds['user']
    )

    print()
    print(f"password={db_creds['password']}")
    print()

    print(f"Connecting to [{db_creds['host']}] at {db_creds['port']} port ...")
    cnx = connector.connect(**db_creds)
    print(f"cnx={cnx}")
    cnx.autocommit = False
    cursor = cnx.cursor()
    print(f"cursor={cursor}")

    try:
        # execute query on that connection
        cursor.execute('SELECT id, make, model, year FROM vehicle limit 5')
        vehicles = cursor.fetchall()
        # print results
        print()
        print(vehicles)
        print()

        # commit connection
        cnx.commit()
    except connector.Error as e:
        # rollback
        cnx.rollback()
        print(e)
    finally:
        # close connection
        cnx.close()
        print(f"Closed Connection.")

except connector.Error as e:
    print(e)
finally:
    print(f"Script Ends.")
