import os
import psycopg2
import csv

# Database credentials
DB_HOST = 'localhost'
DB_NAME = 'medical_data'
DB_USER = 'postgres'
DB_PASSWORD = ''  # Replace with your actual password

# Connect to PostgreSQL with error handling
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("Connection to database established.")
except Exception as e:
    print("Unable to connect to the database.")
    print(e)
    exit(1)

cur = conn.cursor()

# Create the 'photos' table
cur.execute('''
    CREATE TABLE IF NOT EXISTS photos (
        id SERIAL PRIMARY KEY,
        image_name TEXT NOT NULL
    );
''')

# Create the 'yolo_detections' table
cur.execute('''
    CREATE TABLE IF NOT EXISTS yolo_detections (
        id SERIAL PRIMARY KEY,
        image_id INT REFERENCES photos(id),
        name TEXT,
        confidence FLOAT,
        yolo_xmin FLOAT,  -- Changed from xmin to yolo_xmin
        yolo_ymin FLOAT,  -- Changed from ymin to yolo_ymin
        yolo_xmax FLOAT,  -- Changed from xmax to yolo_xmax
        yolo_ymax FLOAT   -- Changed from ymax to yolo_ymax
    );
''')

conn.commit()

# Set folder paths for photos and YOLO detection results
photos_folder = 'C:\Medical-Business-Data-Warehouse\data\photos'  # Adjust path as necessary
yolo_folder = 'C:\Medical-Business-Data-Warehouse\detection_results'  # Adjust path as necessary

# Insert image data and YOLO detection results
for photo_file in sorted(os.listdir(photos_folder)):
    if photo_file.endswith('.jpg'):
        # Insert the image into 'photos' table
        cur.execute('''
            INSERT INTO photos (image_name) VALUES (%s) RETURNING id;
        ''', (photo_file,))
        photo_id = cur.fetchone()[0]

        # Get corresponding YOLO detection CSV file
        yolo_csv_file = os.path.join(yolo_folder, f"{photo_file}_detections.csv")
        
        if os.path.exists(yolo_csv_file):
            with open(yolo_csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Insert YOLO detection result into 'yolo_detections' table
                    cur.execute('''
                        INSERT INTO yolo_detections (
                            image_id, name, confidence, yolo_xmin, yolo_ymin, yolo_xmax, yolo_ymax
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
                    ''', (
                        photo_id,
                        row['name'],
                        float(row['confidence']),  # Convert to float
                        float(row['xmin']),        # Convert to float
                        float(row['ymin']),        # Convert to float
                        float(row['xmax']),        # Convert to float
                        float(row['ymax'])         # Convert to float
                    ))

        conn.commit()

# Close the connection
cur.close()
conn.close()
print("Database population completed.")
