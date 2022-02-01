select * from inspection ins
join etablissement eta on eta.idetablissement = ins.idetablissement
join activite act on act.idactivite = ins.idactivite
order by eta.idetablissement

SELECT count(*) FROM public.activite

select * from public.activite

select count(*) from public.etablissement

select * from public.etablissement

select count(*) from inspection

select * from inspection

select distinct synthese_eval from inspection

select * from inspection, etablissement
where inspection.idetablissement = etablissement.idetablissement
and inspection.synthese_eval = 'A corriger de manière urgente'

update inspection set numero_agrement = null where numero_agrement = 'NaN'

select idetablissement, count(idinspection) as nbAgrements 
from inspection 
where numero_agrement is not null
group by idetablissement
order by nbAgrements desc

select inspection.idetablissement, count(inspection.idinspection) as nbInspections 
from inspection
group by inspection.idetablissement
order by nbInspections desc

select distinct synthese_eval from inspection

select * from etablissement where idetablissement in(18056,16645,10067)

select distinct evolution_score from etablissement order by evolution_score

select * from etablissement order by siret

select * from inspection

select inspection.idetablissement, count(inspection.numero_agrement) as nbAgrements from inspection where numero_agrement is not null group by inspection.idetablissement order by nbAgrements desc

select
	i.synthese_eval
from inspection i
join etablissement e on i.idetablissement = e.idetablissement
join a
