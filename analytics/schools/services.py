import os
import pandas as pd
from django.conf import settings
from .models import School

def populate_database_from_csv():
    csv_file_path = os.path.join(settings.BASE_DIR, 'schools/primaryschool.csv')

    if not School.objects.exists():
        schools_df = pd.read_csv(csv_file_path, usecols=[
            "id", "name", "mgmt", "moi", "cat", "sex", "cluster_name", "block_name", "district_name",
            "school_type", "assembly_name", "parliament_name", "pincode", "address", "landmark", "bus", "coord",
        ])
        School.objects.bulk_create(
            School(**row) for row in schools_df.to_dict(orient='records')
        )
