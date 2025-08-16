-- Database schema for Course Recommendation / Enrollment System
CREATE DATABASE IF NOT EXISTS project;
USE project;

-- Table for streams and sub-streams
CREATE TABLE streams (
    stream VARCHAR(50) NOT NULL,
    sub_stream VARCHAR(50) PRIMARY KEY
);

-- Table for courses under each sub-stream
CREATE TABLE substream (
    sub_stream VARCHAR(50),
    courses VARCHAR(100) NOT NULL,
    top_3_colleges VARCHAR(300),
    average_fees INT,
    FOREIGN KEY (sub_stream) REFERENCES streams(sub_stream)
);
