--поиск по имени или телефону
CREATE OR REPLACE FUNCTION get_contacts_by_patterns(p TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.name, c.phone FROM contacts c
    WHERE c.name ILIKE '%' || p || '%'
    OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

--добавить или обновить контакт
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

--добавить много пользователей сразу
CREATE OR REPLACE PROCEDURE insert_new_users(names VARCHAR[], phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\d+$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;
    IF array_length(invalid_data, 1) IS NOT NULL THEN
        RAISE NOTICE 'Invalid data: %', array_to_string(invalid_data, ',');
    END IF;
END;
$$;

--пагинация
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

--удалить контакт
CREATE OR REPLACE PROCEDURE deleting_contacts(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    ELSE
        RAISE NOTICE 'No name or phone provided!';
    END IF;
END;
$$;

--3.4

--добавить телефон к контакту
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE name = p_name;
    INSERT INTO phones(contact_id, phone, type) VALUES(v_id, p_phone, p_type);
END;
$$;

--переместить контакт в группу
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF NOT EXISTS(SELECT 1 FROM groups WHERE name = p_group) THEN
        INSERT INTO groups(name) VALUES(p_group);
    END IF;
    UPDATE contacts SET group_id = (SELECT id FROM groups WHERE name = p_group)
    WHERE name = p_name;
END;
$$;

--поиск по имени, email и телефону
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.id, c.name, c.phone, c.email
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.name ILIKE '%' || p_query || '%'
    OR c.email ILIKE '%' || p_query || '%'
    OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;

--данные
CALL upsert_contact('Arai', '87767321438');
CALL upsert_contact('Arai2', '87765321438');
CALL upsert_contact('Arai3', '879561438');

CALL add_phone('Arai', '87001234567', 'mobile');
CALL move_to_group('Arai', 'family');

SELECT * FROM get_contacts_by_patterns('776732');
SELECT * FROM get_contacts_paginated(2, 0);
SELECT * FROM search_contacts('Arai');

CALL deleting_contacts(p_name := 'Arai3');
SELECT * FROM contacts;