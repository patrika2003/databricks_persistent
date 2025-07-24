USE DATAANALYTICS;
select * from users;

DELIMITER //

CREATE PROCEDURE GETUSEREMAIL(
    IN pID INT,
    OUT PEMAIL VARCHAR(100)
)
BEGIN
    SELECT email INTO PEMAIL
    FROM users
    WHERE user_id = pID
    LIMIT 1;
END //

DELIMITER ;


-- Call the procedure
SET @output_name = '';
CALL GETPRODUCT(1, @output_name);
SELECT @output_name;

