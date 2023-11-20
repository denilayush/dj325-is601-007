CREATE TABLE
    IS601_Movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        apiId VARCHAR(16) NOT NULL,
        title VARCHAR(128) NOT NULL,
        titleType VARCHAR(16) NOT NULL,
        releaseDate DATE NOT NULL,
        imageUrl VARCHAR(256),
        -- reserved keywords must be wrapped in backticks
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
