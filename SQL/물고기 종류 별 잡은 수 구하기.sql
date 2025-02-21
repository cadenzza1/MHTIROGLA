# '물고기의 종류' 별 물고기의 이름 and 잡은 수
select count(*) as fish_count, N.FISH_NAME
from FISH_NAME_INFO as N
join FISH_INFO as I on N.FISH_TYPE = I.FISH_TYPE
group by N.FISH_NAME
order by 1 desc