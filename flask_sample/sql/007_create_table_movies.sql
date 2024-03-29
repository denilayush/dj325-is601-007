#dj325 18/11/23
CREATE TABLE
    IS601_Movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        api_id VARCHAR(16) UNIQUE,
        title VARCHAR(128) NOT NULL,
        title_type VARCHAR(16) NOT NULL,
        release_date DATE NOT NULL,
        image_url VARCHAR(256),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
