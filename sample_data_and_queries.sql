--sample data:
INSERT INTO streams VALUES ('Science', 'PCM');
INSERT INTO streams VALUES ('Science', 'PCB');
INSERT INTO streams VALUES ('Commerce', 'Commerce');

INSERT INTO substream VALUES ('PCM', 'Computer Science Engineering', 'IIT Bombay, COEP Pune, VIT Vellore', 750000);
INSERT INTO substream VALUES ('PCB', 'MBBS', 'AIIMS Delhi, CMC Vellore, KMC Manipal', 1200000);

--queries:

-- Display all courses under a stream
SELECT courses FROM substream WHERE sub_stream = 'PCM';

-- Update average fees for a course
UPDATE substream SET average_fees = 800000 WHERE courses = 'Computer Science Engineering';

-- Delete a course
DELETE FROM substream WHERE courses = 'Mechanical Engineering';
