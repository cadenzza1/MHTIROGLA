# 2022년도 한 해 평가 점수가 가장 높은 사원!!의 점수, 사번, 성명, 직책, 이메일
# '점수'는 GRADE에 있음. '점수'테이블에서 EMP_NO로 GROUP By한 다음에 SCORE의 SUM이 최대인 사람
SELECT SUM(G.SCORE) as SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_GRADE AS G
JOIN HR_EMPLOYEES AS E on G.EMP_NO = E.EMP_NO
GROUP BY G.EMP_NO
order by 1 DESC
limit 1