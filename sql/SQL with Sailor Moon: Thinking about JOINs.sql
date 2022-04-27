-- Practise some SQL fundamentals by making a simple database on a topic you feel familiar with. Or use mine, populated with a wealth of Sailor Moon trivia.

-- sailorsenshi schema: id, senshi_name, real_name_jpn, school_id, cat_id
-- cats schema: id, name
-- schools schema: id, school

-- Return a results table - sailor_senshi, real_name, cat and school - of all characters, containing each character's high school, their civilian name and the cat who introduced them to their magical crime-fighting destiny.
--Keep in mind some senshi were not initiated by a cat guardian and one is not in high school. The field can be left blank if this is the case.

select senshi_name as sailor_senshi, real_name_jpn as real_name, cats.name as cat, schools.school 
from sailorsenshi left join cats on sailorsenshi.cat_id = cats.id left join
schools on sailorsenshi.school_id = schools.id;
