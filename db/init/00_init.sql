USE bike_sns;
SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_name VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    mail_address VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    profile VARCHAR(300) NOT NULL,
    created_at DATETIME NOT NULL
);

CREATE TABLE posts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    body VARCHAR(1000) NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY fk_user_id(user_id) REFERENCES users(id)
);

CREATE TABLE followings(
    id INT PRIMARY KEY AUTO_INCREMENT,
    following_user_id INT NOT NULL,
    followed_user_id INT NOT NULL,
    FOREIGN KEY fk_following_user_id(following_user_id) REFERENCES users(id),
    FOREIGN KEY fk_followed_user_id(followed_user_id) REFERENCES users(id)
);

CREATE TABLE photos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    order INT NOT NULL,
    FOREIGN KEY fk_post_id(post_id) REFERENCES posts(id)
);

CREATE TABLE good_evaluations(
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    evaluator_user_id INT NOT NULL,
    FOREIGN KEY fk_post_id(post_id) REFERENCES posts(id),
    FOREIGN KEY fk_user_id(evaluator_user_id) REFERENCES users(id)
);

CREATE TABLE comments(
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    body VARCHAR(250) NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY fk_post_id(post_id) REFERENCES posts(id)
);

CREATE TABLE bike_makers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    alphabet_name VARCHAR(20) NOT NULL
);

CREATE TABLE bikes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    maker_id INT NOT NULL,
    engine_capacity_class_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    alphabet_name VARCHAR(100) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    FOREIGN KEY fk_maker_id(maker_id) REFERENCES bike_makers(id),
    FOREIGN KEY fk_engine_capacity_class_id(engine_capacity_class_id) REFERENCES engine_capacity_classes(id)
);

CREATE TABLE engine_capacity_classes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);