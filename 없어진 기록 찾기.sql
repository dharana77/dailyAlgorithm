-- 코드를 입력하세요
SELECT animal_outs.animal_id as ANIMAL_ID, animal_outs.name as NAME FROM ANIMAL_OUTS LEFT JOIN ANIMAL_INS on ANIMAL_OUTS.animal_id = ANIMAL_INS.animal_id where animal_ins.animal_id is null order by animal_outs.animal_id