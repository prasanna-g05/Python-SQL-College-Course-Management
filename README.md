# Python-SQL-College-Course-Management

*Course Recommendation & Enrollment System*
A mini project built in Python with MySQL connectivity that helps students explore courses, colleges, and fees across different streams (Science, Commerce, Arts) and allows administrators to manage course data.

*Features*
1:Student Module:
  Search available streams and sub-streams (e.g., PCM, PCB, Commerce, Arts).

  View detailed information about courses, top colleges, and average fees.

  Fill an enrollment form with personal and academic details.

2: Admin Module:
  Display all course records.

  Insert new course records into the database.

  Update course details (colleges, fees).

  Delete a course from the database.

*Database Design*

Two main tables are used in the project:
  streams → Stores main streams and their sub-streams.
  substream → Stores courses under each sub-stream with details of colleges and average fees.

  CREATE TABLE streams (
      stream VARCHAR(50) NOT NULL,
      sub_stream VARCHAR(50) PRIMARY KEY
  );
  
  CREATE TABLE substream (
      sub_stream VARCHAR(50),
      courses VARCHAR(100) NOT NULL,
      top_3_colleges VARCHAR(300),
      average_fees INT,
      FOREIGN KEY (sub_stream) REFERENCES streams(sub_stream)
  );

*Project Structure*

Python-SQL-Course-Recommendation/
│
├── project.py         # Main Python program
├── schema.sql         # Database structure (CREATE TABLEs)
├── sample_data.sql    # Example INSERT queries
├── queries.sql        # Common SELECT/UPDATE/DELETE queries
└── screenshots/       # (Optional) program output screenshots

*Technologies Used*
  1:Python (mysql-connector, tabulate)
  2:MySQL (database management)

Edit
python project.py
