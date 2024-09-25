CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

CREATE TABLE WorkoutSessions (
    member_id INT,
    date DATE,
    duration_minutes INT,
    calories_burned INT,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
SELECT * FROM Members
SELECT * FROM WorkoutSessions